export OLLAMA_API_BASE="http://localhost:11434"
export OPENAI_API_BASE=http://localhost:11434/v1
export OPENAI_API_KEY=anything

export GOOGLE_API_KEY=""
export GOOGLE_GENAI_USE_VERTEXAI=FALSE

# ollama pull qwen3:latest
# docker run -p 7687:7687 -p 7474:7474 -e NEO4J_PLUGINS='["apoc"]' -e NEO4J_AUTH=neo4j/password neo4j
#export NEO4J_URI=bolt://localhost
export NEO4J_URI=neo4j+s://1a1c5a65.databases.neo4j.io
export NEO4J_URL=$NEO4J_URI
export NEO4J_USERNAME=neo4j
export NEO4J_DATABASE=neo4j
export NEO4J_PASSWORD="StzTyZTC1oaWRnh76hKfkpdRMZl_qk-VdK6d6MLYZtc"
pip install uv
# or curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
uv run adk web
