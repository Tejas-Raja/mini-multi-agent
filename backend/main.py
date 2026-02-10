from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.orchestrator import Orchestrator

app = FastAPI(title="Multi-Agent AI System", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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


@app.websocket("/ws/run")
async def run_agents_ws(websocket: WebSocket):
    await websocket.accept()

    data = await websocket.receive_json()
    task = data.get("task")

    async for message in orchestrator.run_stream(task):
        await websocket.send_json(message)

    await websocket.close()


@app.get("/health")
def health():
    return {"status": "ok"}