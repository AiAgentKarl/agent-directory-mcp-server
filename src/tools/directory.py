"""Directory-Tools — Agent-Service-Verzeichnis."""

from mcp.server.fastmcp import FastMCP

from src import db


def register_directory_tools(mcp: FastMCP):
    """Directory-bezogene MCP-Tools registrieren."""

    @mcp.tool()
    async def register_service(
        name: str,
        description: str,
        category: str,
        capabilities: list[str] = None,
        endpoint: str = None,
        mcp_config: dict = None,
        author: str = None,
        tags: list[str] = None,
    ) -> dict:
        """Einen AI-Agent-Service im Verzeichnis registrieren.

        Args:
            name: Eindeutiger Service-Name
            description: Was der Service macht
            category: Kategorie (z.B. "finance", "weather", "data")
            capabilities: Liste der Fähigkeiten
            endpoint: URL oder MCP-Endpoint
            mcp_config: MCP Server Konfiguration (JSON)
            author: Autor/Entwickler
            tags: Tags für bessere Auffindbarkeit
        """
        return db.register_service(
            name, description, category, capabilities,
            endpoint, mcp_config, author, tags=tags,
        )

    @mcp.tool()
    async def search_services(
        query: str = None,
        category: str = None,
        tags: list[str] = None,
        limit: int = 10,
    ) -> dict:
        """Nach AI-Agent-Services suchen.

        Durchsucht das Verzeichnis nach Services die bestimmte
        Fähigkeiten oder Funktionen bieten.

        Args:
            query: Suchbegriff (durchsucht Name, Beschreibung, Fähigkeiten)
            category: Optional — nur in dieser Kategorie suchen
            tags: Optional — nur Services mit diesen Tags
            limit: Maximale Ergebnisse (Standard: 10)
        """
        results = db.search_services(query, category, tags, limit)
        return {
            "query": query,
            "results_count": len(results),
            "services": results,
        }

    @mcp.tool()
    async def get_service(name: str) -> dict:
        """Details eines bestimmten Service abrufen.

        Args:
            name: Name des Services
        """
        result = db.get_service(name)
        if result:
            return result
        return {"found": False, "name": name}

    @mcp.tool()
    async def rate_service(
        service_name: str,
        rating: int,
        review: str = None,
    ) -> dict:
        """Einen Service bewerten (1-5 Sterne).

        Hilft anderen Agents, gute Services zu finden.

        Args:
            service_name: Name des zu bewertenden Services
            rating: Bewertung 1-5 (5 = beste)
            review: Optionaler Bewertungstext
        """
        if rating < 1 or rating > 5:
            return {"error": "Rating muss zwischen 1 und 5 sein"}
        return db.rate_service(service_name, rating, review)

    @mcp.tool()
    async def list_categories() -> dict:
        """Alle Service-Kategorien auflisten.

        Zeigt welche Kategorien es gibt und wie viele Services
        jeweils registriert sind.
        """
        categories = db.list_categories()
        return {
            "total_categories": len(categories),
            "categories": categories,
        }

    @mcp.tool()
    async def top_services(limit: int = 10) -> dict:
        """Top-bewertete Services anzeigen.

        Die bestbewerteten Services im Verzeichnis.

        Args:
            limit: Anzahl (Standard: 10)
        """
        return {
            "top_services": db.get_top_services(limit),
        }

    @mcp.tool()
    async def directory_stats() -> dict:
        """Verzeichnis-Statistiken abrufen.

        Gesamtzahl Services, Kategorien, Bewertungen.
        """
        return db.get_stats()
