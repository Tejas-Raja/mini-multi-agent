from langchain_core.messages import SystemMessage, HumanMessage
from config import get_llm
from prompts import PLANNER_PROMPT

class PlannerAgent:
    def __init__(self):
        self.llm = get_llm()

    async def run(self, research: str):
        messages = [
            SystemMessage(content=PLANNER_PROMPT),
            HumanMessage(content=research)
        ]
        response = await self.llm.ainvoke(messages)
        return response.content