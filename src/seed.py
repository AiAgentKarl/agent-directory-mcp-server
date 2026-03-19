"""Seed-Daten — Verzeichnis mit bekannten MCP-Servern vorbeladen."""

from src.db import register_service


def seed_directory():
    """Initiale Services ins Verzeichnis laden."""
    services = [
        {
            "name": "solana-mcp-server",
            "description": "Solana blockchain data — wallets, token prices, DeFi yields, safety checks, whale tracking",
            "category": "finance",
            "capabilities": ["wallet_balance", "token_price", "defi_yields", "token_safety", "whale_tracking"],
            "endpoint": "https://github.com/AiAgentKarl/solana-mcp-server",
            "mcp_config": {"command": "uvx", "args": ["solana-mcp-server"]},
            "author": "AiAgentKarl",
            "tags": ["crypto", "solana", "defi", "blockchain"],
        },
        {
            "name": "germany-mcp-server",
            "description": "German open data — Destatis, Bundesanzeiger, weather, energy, COVID stats",
            "category": "government",
            "capabilities": ["statistics", "company_filings", "weather", "energy_data"],
            "endpoint": "https://github.com/AiAgentKarl/germany-mcp-server",
            "mcp_config": {"command": "uvx", "args": ["germany-mcp-server"]},
            "author": "AiAgentKarl",
            "tags": ["germany", "open-data", "statistics"],
        },
        {
            "name": "agriculture-mcp-server",
            "description": "Global agriculture data — crop production, soil data, food prices, farm weather",
            "category": "agriculture",
            "capabilities": ["crop_data", "soil_analysis", "food_prices", "farm_weather"],
            "endpoint": "https://github.com/AiAgentKarl/agriculture-mcp-server",
            "mcp_config": {"command": "uvx", "args": ["agriculture-mcp-server"]},
            "author": "AiAgentKarl",
            "tags": ["agriculture", "farming", "food", "climate"],
        },
        {
            "name": "eu-company-mcp-server",
            "description": "European company data — business registers, LEI lookup, financial filings",
            "category": "business",
            "capabilities": ["company_search", "financial_filings", "lei_lookup", "beneficial_owners"],
            "endpoint": "https://github.com/AiAgentKarl/eu-company-mcp-server",
            "mcp_config": {"command": "uvx", "args": ["eu-company-mcp-server"]},
            "author": "AiAgentKarl",
            "tags": ["business", "europe", "companies", "due-diligence"],
        },
        {
            "name": "space-mcp-server",
            "description": "NASA & ESA space data — asteroids, Mars rovers, space weather, exoplanets",
            "category": "science",
            "capabilities": ["asteroids", "mars_photos", "space_weather", "exoplanets", "apod"],
            "endpoint": "https://github.com/AiAgentKarl/space-mcp-server",
            "mcp_config": {"command": "uvx", "args": ["space-mcp-server"]},
            "author": "AiAgentKarl",
            "tags": ["space", "nasa", "astronomy", "science"],
        },
        {
            "name": "aviation-mcp-server",
            "description": "Aviation data — flight tracking, airports, airlines, aircraft",
            "category": "transport",
            "capabilities": ["flight_tracking", "airport_info", "airline_data", "aircraft_details"],
            "endpoint": "https://github.com/AiAgentKarl/aviation-mcp-server",
            "mcp_config": {"command": "uvx", "args": ["aviation-mcp-server"]},
            "author": "AiAgentKarl",
            "tags": ["aviation", "flights", "airports", "travel"],
        },
        {
            "name": "openmeteo-mcp-server",
            "description": "Global weather — forecasts, air quality, historical data, marine weather",
            "category": "weather",
            "capabilities": ["current_weather", "forecast", "air_quality", "historical", "marine"],
            "endpoint": "https://github.com/AiAgentKarl/weather-mcp-server",
            "mcp_config": {"command": "uvx", "args": ["openmeteo-mcp-server"]},
            "author": "AiAgentKarl",
            "tags": ["weather", "climate", "forecast", "air-quality"],
        },
        {
            "name": "x402-mcp-server",
            "description": "x402 micropayment gateway — USDC payments between AI agents on Solana",
            "category": "payments",
            "capabilities": ["payment_requests", "on_chain_verify", "pricing", "revenue_tracking"],
            "endpoint": "https://github.com/AiAgentKarl/x402-mcp-server",
            "mcp_config": {"command": "uvx", "args": ["x402-mcp-server"]},
            "author": "AiAgentKarl",
            "tags": ["payments", "x402", "micropayments", "usdc"],
        },
        {
            "name": "agent-memory-mcp-server",
            "description": "Persistent memory for AI agents — survives across sessions with search and tags",
            "category": "infrastructure",
            "capabilities": ["store", "retrieve", "search", "namespaces", "tags"],
            "endpoint": "https://github.com/AiAgentKarl/agent-memory-mcp-server",
            "mcp_config": {"command": "uvx", "args": ["agent-memory-mcp-server"]},
            "author": "AiAgentKarl",
            "tags": ["memory", "persistence", "knowledge", "infrastructure"],
        },
        {
            "name": "agent-directory-mcp-server",
            "description": "Agent-to-Agent service directory — discover, register and rate AI services",
            "category": "infrastructure",
            "capabilities": ["register", "search", "rate", "discover"],
            "endpoint": "https://github.com/AiAgentKarl/agent-directory-mcp-server",
            "mcp_config": {"command": "uvx", "args": ["agent-directory-mcp-server"]},
            "author": "AiAgentKarl",
            "tags": ["directory", "discovery", "marketplace", "infrastructure"],
        },
        {
            "name": "agent-analytics-mcp-server",
            "description": "Usage analytics for AI agent tools — dashboards, per-tool stats, error tracking",
            "category": "infrastructure",
            "capabilities": ["track_events", "dashboard", "tool_analytics", "agent_analytics"],
            "endpoint": "https://github.com/AiAgentKarl/agent-analytics-mcp-server",
            "mcp_config": {"command": "uvx", "args": ["agent-analytics-mcp-server"]},
            "author": "AiAgentKarl",
            "tags": ["analytics", "monitoring", "tracking", "infrastructure"],
        },
    ]

    for s in services:
        register_service(**s)

    return {"seeded": len(services), "services": [s["name"] for s in services]}
