## Agent Development Kit (ADK) and MCP Test

This repository contains some basic test code for Agent Development Kit (ADK) and the Model Context Protocol (MCP) Servers.

### Hello World Agent

Simple agent with these tools:

* Rolling dice
* Base 64 encoding 
* Doodle access from a file / URL

```shell
uv run adk web
```

### Memory Agent

Simple Agent that access MCP STDIO Tools and uses neo4j-mcp-cypher to access a memory Neo4j knowledge graph.

Add a `neo4j-memory.env` with Database connection information:

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
# OPENAPI_API_KEY=your_openapi_key
# ANTHROPIC_API_KEY=your_anthropic_key
```

Then run the agent:

```shell
uv run adk web
```

### More Advanced MCP + ADK Agent

Uses the Diffbot Companies+Articles dataset and the MCP Toolbox to access a Neo4j knowledge graph with company data.

Multi-Agent Setup with 3 Agents

* Database Agent
* Investment Agent
* Investor Research Agent
* Root Agent

Tools

* Python tools for database access
* MCP Toolbox for accessing the knowledge graph with predefined tools

* [Blog Post](https://www.googlecloudcommunity.com/gc/Cloud-Product-Articles/Using-Google-s-Agent-Development-Kit-ADK-with-MCP-Toolbox-and/ta-p/898512)
* [GitHub Repository](https://github.com/neo4j-examples/neo4j-gcp-vertex-ai-langchain/tree/main/neo4j-agent-development-kit-adk-companies)