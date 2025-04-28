from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.langchain import LangChainLLM
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from langchain_ollama import ChatOllama


from papermate_agent import PaperMateAgent

if __name__ == "__main__": 
    #add you path directory here
    agent = PaperMateAgent(docs_path="...")

    print("📄 PaperMate is ready. Ask your questions. Type 'exit' to quit.\n")

    while True:
        question = input("❓ Ask PaperMate: ")

        if question.lower() in ["exit", "quit"]:
            break

        if question.lower() == "recall":
            print("\n🗃 Memory Recall:\n")
            agent.recall_memory()
            continue

        print("❓ Asking:", question)
        answer = agent.ask(question)

        print("\n🧠 Final Answer:\n", answer)

"""
# Step 1: Load documents
documents = SimpleDirectoryReader( input_dir="....", recursive=True).load_data()

# Step 2: Create embedding model
embed_model = HuggingFaceEmbedding(model_name="all-MiniLM-L6-v2")

# Step 3: Build vector index
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

# Step 4: Initialize LLM
llm = ChatOllama(model="deepseek-r1")  
wrapped_llm = LangChainLLM(llm=llm)

# Step 5: Create query engine
query_engine = index.as_query_engine(llm=wrapped_llm)

# Step 6: Ask a question
response = query_engine.query("What is memory sharing in retrieval-augmented generation?")
print("🧠 Answer:", response)
"""
