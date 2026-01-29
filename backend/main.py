from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from orchestrator import Orchestrator

app = FastAPI(title="Multi-Agent AI System", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = Orchestrator()

class TaskRequest(BaseModel):
    task: str

@app.post("/api/v1/run")
async def run_task(req: TaskRequest):
    return await orchestrator.run(req.task)

@app.get("/health")
def health():
    return {"status": "ok"}