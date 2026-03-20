# Agent Directory MCP Server 📇

Agent-to-Agent service directory — a **Yellow Pages for AI agents**. Discover, register, and rate AI services.

## The Problem

AI agents need to find other agents/services to collaborate with. There's no standardized way for agents to discover what services are available and which are trustworthy.

## Features

- **Register Services** — Add your agent/service to the directory
- **Search & Discover** — Find services by capability, category, or keyword
- **Ratings & Reviews** — Community-driven quality signals
- **Categories** — Organized by domain (finance, weather, data, etc.)
- **MCP Config** — Services include their MCP configuration for instant setup

## Installation

```bash
pip install agent-directory-mcp-server
```

## Usage with Claude Code

```json
{
  "mcpServers": {
    "directory": {
      "command": "uvx",
      "args": ["agent-directory-mcp-server"]
    }
  }
}
```

## Tools

| Tool | Description |
|------|-------------|
| `register_service` | Register a service in the directory |
| `search_services` | Search for services by keyword/category |
| `get_service` | Get details of a specific service |
| `rate_service` | Rate a service (1-5 stars) |
| `list_categories` | List all service categories |
| `top_services` | Show highest-rated services |
| `directory_stats` | Directory statistics |

## Network Effect

The more services registered, the more useful the directory becomes. The more agents use it for discovery, the more valuable it is to register. This creates a flywheel effect that makes early adoption especially valuable.


---

## More MCP Servers by AiAgentKarl

| Category | Servers |
|----------|---------|
| 🔗 Blockchain | [Solana](https://github.com/AiAgentKarl/solana-mcp-server) |
| 🌍 Data | [Weather](https://github.com/AiAgentKarl/weather-mcp-server) · [Germany](https://github.com/AiAgentKarl/germany-mcp-server) · [Agriculture](https://github.com/AiAgentKarl/agriculture-mcp-server) · [Space](https://github.com/AiAgentKarl/space-mcp-server) · [Aviation](https://github.com/AiAgentKarl/aviation-mcp-server) · [EU Companies](https://github.com/AiAgentKarl/eu-company-mcp-server) |
| 🔒 Security | [Cybersecurity](https://github.com/AiAgentKarl/cybersecurity-mcp-server) · [Policy Gateway](https://github.com/AiAgentKarl/agent-policy-gateway-mcp) · [Audit Trail](https://github.com/AiAgentKarl/agent-audit-trail-mcp) |
| 🤖 Agent Infra | [Memory](https://github.com/AiAgentKarl/agent-memory-mcp-server) · [Directory](https://github.com/AiAgentKarl/agent-directory-mcp-server) · [Hub](https://github.com/AiAgentKarl/mcp-appstore-server) · [Reputation](https://github.com/AiAgentKarl/agent-reputation-mcp-server) |
| 🔬 Research | [Academic](https://github.com/AiAgentKarl/crossref-academic-mcp-server) · [LLM Benchmark](https://github.com/AiAgentKarl/llm-benchmark-mcp-server) · [Legal](https://github.com/AiAgentKarl/legal-court-mcp-server) |

[→ Full catalog (40+ servers)](https://github.com/AiAgentKarl)

## License

MIT
