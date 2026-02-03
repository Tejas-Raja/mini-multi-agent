import { useState } from "react";
import { runAgents } from "./api";
import PromptBox from "./components/PromptBox";
import AgentPanel from "./components/AgentPanel";
import FinalOutput from "./components/FinalOutput";

function App() {
  const [logs, setLogs] = useState([]);
  const [finalOutput, setFinalOutput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleRun = async (task) => {
    setLoading(true);
    setLogs([]);
    setFinalOutput("");

    try {
      const result = await runAgents(task);
      setLogs(result.logs);
      setFinalOutput(result.final);
    } catch (err) {
      alert("Error calling backend");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: "900px", margin: "auto", padding: "20px" }}>
      <h1>Multi-Agent AI System</h1>

      <PromptBox onSubmit={handleRun} loading={loading} />

      {logs.map((log, idx) => (
        <AgentPanel
          key={idx}
          agent={log.agent}
          content={log.content}
        />
      ))}

      <FinalOutput content={finalOutput} />
    </div>
  );
}

export default App;