"""Datenbank — SQLite-basiertes Agent/Service-Verzeichnis."""

import sqlite3
import json
import os
from datetime import datetime, timezone
from pathlib import Path


_DB_PATH = os.getenv("DIRECTORY_DB_PATH", str(Path(__file__).resolve().parent.parent / "directory.db"))


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(_DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            capabilities TEXT,
            endpoint TEXT,
            mcp_config TEXT,
            author TEXT,
            version TEXT DEFAULT '0.1.0',
            tags TEXT,
            avg_rating REAL DEFAULT 0,
            total_ratings INTEGER DEFAULT 0,
            total_calls INTEGER DEFAULT 0,
            registered_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            active INTEGER DEFAULT 1
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_name TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
            review TEXT,
            rater_id TEXT,
            created_at TEXT NOT NULL
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_category ON services(category)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_tags ON services(tags)")
    conn.commit()
    return conn


def register_service(
    name: str,
    description: str,
    category: str,
    capabilities: list[str] = None,
    endpoint: str = None,
    mcp_config: dict = None,
    author: str = None,
    version: str = "0.1.0",
    tags: list[str] = None,
) -> dict:
    """Service registrieren oder aktualisieren."""
    conn = _connect()
    now = datetime.now(timezone.utc).isoformat()
    conn.execute(
        """INSERT INTO services
           (name, description, category, capabilities, endpoint,
            mcp_config, author, version, tags, registered_at, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
           ON CONFLICT(name) DO UPDATE SET
               description=excluded.description,
               category=excluded.category,
               capabilities=excluded.capabilities,
               endpoint=excluded.endpoint,
               mcp_config=excluded.mcp_config,
               author=excluded.author,
               version=excluded.version,
               tags=excluded.tags,
               updated_at=excluded.updated_at""",
        (name, description, category,
         json.dumps(capabilities) if capabilities else None,
         endpoint,
         json.dumps(mcp_config) if mcp_config else None,
         author, version,
         json.dumps(tags) if tags else None,
         now, now),
    )
    conn.commit()
    conn.close()
    return {"name": name, "registered": True, "updated_at": now}


def search_services(
    query: str = None,
    category: str = None,
    tags: list[str] = None,
    limit: int = 20,
) -> list:
    """Services suchen."""
    conn = _connect()
    sql = "SELECT * FROM services WHERE active=1"
    params = []

    if query:
        sql += " AND (name LIKE ? OR description LIKE ? OR capabilities LIKE ?)"
        params.extend([f"%{query}%"] * 3)

    if category:
        sql += " AND category=?"
        params.append(category)

    if tags:
        for tag in tags:
            sql += " AND tags LIKE ?"
            params.append(f"%{tag}%")

    sql += " ORDER BY avg_rating DESC, total_calls DESC LIMIT ?"
    params.append(limit)

    rows = conn.execute(sql, params).fetchall()
    conn.close()

    results = []
    for r in rows:
        d = dict(r)
        d["capabilities"] = json.loads(d["capabilities"]) if d["capabilities"] else []
        d["tags"] = json.loads(d["tags"]) if d["tags"] else []
        d["mcp_config"] = json.loads(d["mcp_config"]) if d["mcp_config"] else None
        results.append(d)
    return results


def get_service(name: str) -> dict | None:
    """Service-Details abrufen."""
    conn = _connect()
    row = conn.execute("SELECT * FROM services WHERE name=?", (name,)).fetchone()
    if row:
        # Call-Counter erhöhen
        conn.execute("UPDATE services SET total_calls = total_calls + 1 WHERE name=?", (name,))
        conn.commit()
    conn.close()

    if row:
        d = dict(row)
        d["capabilities"] = json.loads(d["capabilities"]) if d["capabilities"] else []
        d["tags"] = json.loads(d["tags"]) if d["tags"] else []
        d["mcp_config"] = json.loads(d["mcp_config"]) if d["mcp_config"] else None
        return d
    return None


def rate_service(service_name: str, rating: int, review: str = None, rater_id: str = None) -> dict:
    """Service bewerten (1-5 Sterne)."""
    conn = _connect()
    now = datetime.now(timezone.utc).isoformat()
    conn.execute(
        "INSERT INTO ratings (service_name, rating, review, rater_id, created_at) VALUES (?, ?, ?, ?, ?)",
        (service_name, rating, review, rater_id, now),
    )
    # Durchschnitt neu berechnen
    result = conn.execute(
        "SELECT AVG(rating) as avg, COUNT(*) as cnt FROM ratings WHERE service_name=?",
        (service_name,),
    ).fetchone()
    conn.execute(
        "UPDATE services SET avg_rating=?, total_ratings=? WHERE name=?",
        (round(result["avg"], 2), result["cnt"], service_name),
    )
    conn.commit()
    conn.close()
    return {"service": service_name, "rating": rating, "new_avg": round(result["avg"], 2)}


def list_categories() -> list:
    """Alle Kategorien mit Anzahl Services."""
    conn = _connect()
    rows = conn.execute(
        "SELECT category, COUNT(*) as count FROM services WHERE active=1 GROUP BY category ORDER BY count DESC"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_top_services(limit: int = 10) -> list:
    """Top-bewertete Services."""
    conn = _connect()
    rows = conn.execute(
        "SELECT name, category, avg_rating, total_ratings, total_calls FROM services WHERE active=1 AND total_ratings > 0 ORDER BY avg_rating DESC LIMIT ?",
        (limit,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_stats() -> dict:
    """Verzeichnis-Statistiken."""
    conn = _connect()
    total = conn.execute("SELECT COUNT(*) as c FROM services WHERE active=1").fetchone()["c"]
    categories = conn.execute("SELECT COUNT(DISTINCT category) as c FROM services").fetchone()["c"]
    total_ratings = conn.execute("SELECT COUNT(*) as c FROM ratings").fetchone()["c"]
    conn.close()
    return {
        "total_services": total,
        "total_categories": categories,
        "total_ratings": total_ratings,
    }
