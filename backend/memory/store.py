class MemoryStore:
    def __init__(self):
        self.history = []

    def add(self, agent: str, content: str):
        self.history.append({
            "agent": agent,
            "content": content
        })

    def get_context(self):
        context = ""
        for h in self.history:
            context += f"{h['agent']}:\n{h['content']}\n\n"
        return context

    def clear(self):
        self.history = []
