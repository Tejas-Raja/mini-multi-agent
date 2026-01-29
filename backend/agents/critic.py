from langchain_core.messages import SystemMessage, HumanMessage
from config import get_llm
from prompts import CRITIC_PROMPT

class CriticAgent:
    def __init__(self):
        self.llm = get_llm()

    async def run(self, content: str):
        messages = [
            SystemMessage(content=CRITIC_PROMPT),
            HumanMessage(content=content)
        ]
        response = await self.llm.ainvoke(messages)
        return response.content