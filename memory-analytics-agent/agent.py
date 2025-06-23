import dotenv
import os

from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

dotenv.load_dotenv("../neo4j-memory.env")

root_agent = Agent(
    name="memory_analytics_agent",
    # model="gemini-2.5-pro",
    model = "gemini-2.5-flash",
    # model=LiteLlm(model="openai/gpt-4.1"),
    # model=LiteLlm(model="anthropic/claude-sonnet-4-20250514"),
    description="""
    Agent to access a database with conversational and fact memories as Memory entities with observations 
    and relationships stored in a knowledge graph. To analyse the memories with plain Neo4j cypher to determine 
    insights about the accumulated memories.
    """,
    instruction="""
    You are an assistant with access to a graph database with connected memory entities. 
    Generate and execute analytical Cypher queries based on the schema to read memory entities and their relationships and generate sensible summaries if asked for.
    """,
    tools=[MCPToolset(
        connection_params=StdioServerParameters(
            command='uvx',
            args=[
                "mcp-neo4j-cypher",
            ],
            env={ k: os.environ[k] for k in ["NEO4J_URI","NEO4J_USERNAME","NEO4J_PASSWORD"] }
        ),
        tool_filter=['get_neo4j_schema','read_neo4j_cypher']
    )]
)