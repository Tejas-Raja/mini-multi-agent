from backend.agents.researcher import ResearcherAgent
from backend.agents.planner import PlannerAgent
from backend.agents.writer import WriterAgent
from backend.agents.critic import CriticAgent
from backend.memory.store import MemoryStore

class Orchestrator:
    def __init__(self, max_iterations=1):
        self.researcher = ResearcherAgent()
        self.planner = PlannerAgent()
        self.writer = WriterAgent()
        self.critic = CriticAgent()

    async def run_stream(self, task: str):
        # Researcher
        research = await self.researcher.run(task)
        yield {
            "agent": "Researcher",
            "type": "done",
            "content": research
        }

        # Planner
        plan = await self.planner.run(research)
        yield {
            "agent": "Planner",
            "type": "done",
            "content": plan
        }

        # Writer (draft)
        draft = await self.writer.run(plan)
        yield {
            "agent": "Writer",
            "type": "done",
            "content": draft
        }

        # Critic
        critique = await self.critic.run(draft)
        yield {
            "agent": "Critic",
            "type": "done",
            "content": critique
        }

        # Writer (final)
        improved = await self.writer.run(
            f"Improve the following based on critique:\n{critique}\n\n{draft}"
        )

        yield {
            "agent": "Final",
            "type": "final",
            "content": improved
        }
