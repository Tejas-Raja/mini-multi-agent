import axios from "axios";

const API_BASE = "https://multi-agent-ai-backend.onrender.com";

export const runAgents = async (task) => {
  const res = await axios.post(`${API_BASE}/api/v1/run`, {
    task: task,
  });
  return res.data;
};