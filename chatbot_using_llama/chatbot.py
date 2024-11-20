from fastapi import FastAPI
from langserve import add_routes
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import uvicorn
import os
from dotenv import load_dotenv

os.environ["LANGCHAIN_API_KEY"] = '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'

# Verify that the API key is set
if os.environ["LANGCHAIN_API_KEY"] is None:
    raise ValueError("LANGCHAIN_API_KEY is not set.")

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title = "Simple Server",
    version = '1.0',
    description = "My first api server"
)

llm = Ollama(model = "llama3.1")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

add_routes(
    app,
    prompt | llm,
    path = "/prompt"
)

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
