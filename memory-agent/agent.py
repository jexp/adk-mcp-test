import dotenv
import os

from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

dotenv.load_dotenv("neo4j-memory.env")

root_agent = Agent(
    name="memory_agent",
    # model="gemini-2.0-flash-exp",
    # model=LiteLlm(model="openai/gpt-4o"),
    model=LiteLlm(model="anthropic/claude-sonnet-4-20250514"),
    description="""
    Agent to access conversational and fact memories as Memory entities with observations 
    and relationships stored in a knowledge graph.
    """,
    instruction="""
    You are an assistant with access to a graph database with connected memory entities. 
    Generate and execute Cypher queries based on the schema to read memory entities and their relationships.
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