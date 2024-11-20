from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set up environment variables for Langchain
os.environ["LANGCHAIN_API_KEY"] = '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'
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A Simple API Server"
)


# Initialize Ollama LLM model
llm = Ollama(model="llama3.1")

# Create a prompt template
prompt = ChatPromptTemplate.from_template("Write information about {topic}.")

# Add routes for custom LLM prompt
add_routes(
    app,
    prompt | llm,
    path="/info"
)

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
