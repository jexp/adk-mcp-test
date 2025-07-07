## Agent Development Kit (ADK) and MCP Test

This repository contains some basic test code for Agent Development Kit (ADK) and the Model Context Protocol (MCP) Servers.

### Getting started

The easiest way to run this repository is to open an [GitHub CodeSpace](https://codespaces.new/jexp/adk-mcp-test) on this repository.
Edit `run.sh` for the environment variables (`GOOGLE_API_KEY, NEO4J_URI, NEO4J_PASSWORD`) and execute `./run.sh`.
Then open the forwarded port URL in your browser. (See also `Ports` tab in the terminal)

### Hello World Agent

Simple agent with these tools:

* Rolling dice
* Base 64 encoding 
* Doodle access from a file / URL

```shell
# run.sh exports the neccessary env variables, and runs the command below to start the ADK developer UI
./run.sh
# it also runs the command below to start the ADK developer UI
# uv run adk web
```

### ADK Config

Either edit the environment variables in `run.sh` and run it directly.

```shell
# run.sh exports the neccessary env variables
# also runs uv sync and uv run adk web

./run.sh
```

<details>
  <summary>Config via env file</summary>
  
#### Config via env file

Or add a `neo4j-memory.env` with Database connection information and API keys:

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
GOOGLE_API_KEY="the google api key"
# OPENAPI_API_KEY=your_openapi_key
# ANTHROPIC_API_KEY=your_anthropic_key
```

Then run the agent:

```shell
uv run adk web
```
</details>

### Memory Agent

Simple Agent that access MCP STDIO Tools and uses `neo4j-mcp-memory` to maintian a conversational memory Neo4j knowledge graph.

### Memory Analytics Agent

Agent that users `mcp-neo4j-cypher` a generic database access MCP Server to run any query on our created memories.

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
