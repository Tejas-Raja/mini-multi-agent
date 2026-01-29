from langchain_core.messages import SystemMessage, HumanMessage
from backend.config import get_llm
from backend.prompts import WRITER_PROMPT

class WriterAgent:
    def __init__(self):
        self.llm = get_llm()

    async def run(self, plan: str):
        messages = [
            SystemMessage(content=WRITER_PROMPT),
            HumanMessage(content=plan)
        ]
        response = await self.llm.ainvoke(messages)
        return response.content