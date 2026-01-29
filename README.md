# Multi-Agent AI System (LangChain)

A collaborative multi-agent AI system built with LangChain and FastAPI.

## Agents
- Researcher
- Planner
- Writer
- Critic

## Features
- Role-based agents
- Iterative critique & improvement loop
- Shared memory
- Transparent agent collaboration
- Gemini LLM backend

## Tech Stack
- Python 3.12
- FastAPI
- LangChain
- Google Gemini API

## Run Locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
