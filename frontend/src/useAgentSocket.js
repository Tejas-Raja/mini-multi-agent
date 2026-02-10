export function useAgentSocket(onMessage) {
  const connect = (task) => {
    const ws = new WebSocket(
      "wss://multi-agent-ai-backend.onrender.com/ws/run"
    );

    ws.onopen = () => {
      ws.send(JSON.stringify({ task }));
    };

    ws.onmessage = (event) => {
      onMessage(JSON.parse(event.data));
    };

    return ws;
  };

  return { connect };
}
