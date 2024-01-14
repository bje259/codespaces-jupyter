from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
#from neo4j_vector_memory import chain as neo4j_vector_memory_chain
#from pirate_speak.chain import chain as pirate_speak_chain
#from openai_functions_agent import agent_executor as openai_functions_agent_chain
#from rag_conversation import chain as rag_conversation_chain
from rag_conversation_zep import chain as rag_conversation_zep_chain

#add_routes(app, neo4j_vector_memory_chain, path="/neo4j-vector-memory")
#add_routes(app, pirate_speak_chain, path="/pirate-speak")
#add_routes(app, openai_functions_agent_chain, path="/openai-functions-agent")
#add_routes(app, rag_conversation_chain, path="/rag-conversation")
add_routes(app, rag_conversation_zep_chain, path="/rag-conversation-zep")

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, NotImplemented)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8333)
