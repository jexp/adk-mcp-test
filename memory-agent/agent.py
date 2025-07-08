import dotenv
import os

from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

dotenv.load_dotenv("../neo4j-memory.env")

root_agent = Agent(
    name="memory_agent",
    # model="gemini-2.5-pro",
    model = "gemini-2.5-flash",
    # model=LiteLlm(model="openai/gpt-4.1"),
    # model=LiteLlm(model="anthropic/claude-sonnet-4-20250514"),
    description="""
    Agent to retrieve, store and update conversational and factual memories as Memory entities with observations 
    and relationships stored in a knowledge graph.
    """,
    instruction="""
    You are an assistant with access to a knowledge graph with connected memory entities. 
    You can add, remove, update memories and relationships with the appropriate tools.
    """,
    tools=[MCPToolset(
        connection_params=StdioServerParameters(
            command='uvx',
            args=[
                "mcp-neo4j-memory",
            ],
            env={ k: os.environ[k] for k in ["NEO4J_URL","NEO4J_USERNAME","NEO4J_PASSWORD"] }
        ),
    )]
)