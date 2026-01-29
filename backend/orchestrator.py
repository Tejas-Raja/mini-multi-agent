from backend.agents.researcher import ResearcherAgent
from backend.agents.planner import PlannerAgent
from backend.agents.writer import WriterAgent
from backend.agents.critic import CriticAgent
from backend.memory.store import MemoryStore

class Orchestrator:
    def __init__(self, max_iterations=2):
        self.researcher = ResearcherAgent()
        self.planner = PlannerAgent()
        self.writer = WriterAgent()
        self.critic = CriticAgent()
        self.memory = MemoryStore()
        self.max_iterations = max_iterations

    async def run(self, task: str):
        self.memory.clear()

        research = await self.researcher.run(task)
        self.memory.add("Researcher", research)

        plan_input = self.memory.get_context()
        plan = await self.planner.run(plan_input)
        self.memory.add("Planner", plan)

        draft_input = self.memory.get_context()
        draft = await self.writer.run(draft_input)
        self.memory.add("Writer", draft)

        for _ in range(self.max_iterations):
            critique_input = self.memory.get_context()
            critique = await self.critic.run(critique_input)
            self.memory.add("Critic", critique)

            improve_input = self.memory.get_context() + "\nImprove the content based on critique."
            draft = await self.writer.run(improve_input)
            self.memory.add("Writer", draft)

        return {
            "final": draft,
            "logs": self.memory.history
        }
