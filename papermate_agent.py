# papermate_agent.py

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.langchain import LangChainLLM
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from memory_store import MemoryStore

class PaperMateAgent:
    def __init__(self, docs_path: str):
        self.docs_path = docs_path
        self.memory_store = MemoryStore()
        self.memory_store.load("memory.json")
        self._setup()

    def _setup(self):
        print("Loading documents...")
        documents = SimpleDirectoryReader(self.docs_path, recursive=True).load_data()
        
        print("Setting up embed model & LLM...")
        embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        llm = ChatOllama(model="deepseek-r1")
        wrapped_llm = LangChainLLM(llm=llm)

        print("Building index...")
        self.index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
        self.query_engine = self.index.as_query_engine(llm=wrapped_llm)

    def ask(self, query: str) -> str:
        print(f"❓ Asking: {query}")
        response = self.query_engine.query(query)
        answer = str(response)
        print("💭 Reflecting on answer...")
        self._reflect(query, answer)
        return answer

    def _reflect(self, query: str, answer: str):
        print("📝 Reflecting and saving to memory...")
        self.memory_store.reflect(query, answer)
        self.memory_store.save("memory.json")  # Persist memory after each interaction

    def recall_memory(self):
        memories = self.memory_store.get_all()
        if not memories:
            print("🫙 No memory yet!")
            return

        print(" Memory so far:")
        for i, mem in enumerate(memories, 1):
            print(f"\n🔹 Memory {i}:\nQ: {mem['question']}\nA: {mem['answer']}")
