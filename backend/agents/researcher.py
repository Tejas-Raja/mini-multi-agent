from langchain_core.messages import SystemMessage, HumanMessage
from backend.config import get_llm
from backend.prompts import RESEARCHER_PROMPT

class ResearcherAgent:
    def __init__(self):
        self.llm = get_llm()

    async def run(self, task: str):
        messages = [
            SystemMessage(content=RESEARCHER_PROMPT),
            HumanMessage(content=task)
        ]
        response = await self.llm.ainvoke(messages)
        return response.content