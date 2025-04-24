import json

class MemoryStore:
    def __init__(self):
        self.memory = []
    

    def reflect(self, question, answer):
        print(f"🧠 Storing Q: {question}")
        self.memory.append({"question": question, "answer": answer})

    def save(self, path):
        print(f"💾 Saving memory to: {path}")
        with open(path, "w") as f:
            json.dump(self.memory, f, indent=2)

    def load(self, path):
        try:
            with open(path, "r") as f:
                self.memory = json.load(f)
        except FileNotFoundError:
            self.memory = []

    def recall(self):
        for i, entry in enumerate(self.memory, 1):
            print(f"🗃 Memory {i}:")
            print(f"Q: {entry['question']}")
            print(f"A: {entry['answer']}\n")
    def get_all(self):
        return self.memory
