"""Agent Directory MCP Server — Service-Verzeichnis für AI-Agents."""

from mcp.server.fastmcp import FastMCP

from src.tools.directory import register_directory_tools

mcp = FastMCP(
    "Agent Directory",
    instructions=(
        "Agent-to-Agent service directory. Register your AI services, "
        "discover other agents' capabilities, and rate services. "
        "Think of it as a Yellow Pages for AI agents."
    ),
)

register_directory_tools(mcp)


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
