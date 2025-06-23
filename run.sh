export OLLAMA_API_BASE="http://localhost:11434"
export OPENAI_API_BASE=http://localhost:11434/v1
export OPENAI_API_KEY=anything

export GOOGLE_API_KEY=""
export GOOGLE_GENAI_USE_VERTEXAI=FALSE

# ollama pull qwen3:latest
# docker run -p 7687:7687 -p 7474:7474 -e NEO4J_PLUGINS='["apoc"]' -e NEO4J_AUTH=neo4j/password neo4j
#export NEO4J_URI=bolt://localhost
export NEO4J_URI=neo4j+s://fda2b1c4.databases.neo4j.io
export NEO4J_USERNAME=neo4j
export NEO4J_DATABASE=neo4j
export NEO4J_PASSWORD="L8ZkmVZFj_rk3WwVKc73EEXsEk0Y-vEyxzoQAhm3DHg"
uv sync
uv run adk web