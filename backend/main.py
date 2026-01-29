from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import Orchestrator

app = FastAPI()
orchestrator = Orchestrator()

class TaskRequest(BaseModel):
    task: str

@app.post("/run")
async def run_task(req: TaskRequest):
    result = await orchestrator.run(req.task)
    return result