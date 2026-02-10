import { useState } from "react";
import PromptBox from "./components/PromptBox";
import AgentPanel from "./components/AgentPanel";
import FinalOutput from "./components/FinalOutput";
import { useAgentSocket } from "./useAgentSocket";
import { typeText } from "./utils/typewriter";

function App() {
  const [agents, setAgents] = useState({});
  const [finalAnswer, setFinalAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleMessage = (msg) => {
    if (msg.type === "final") {
      typeText(msg.content, setFinalAnswer);
      setLoading(false);
      return;
    }

    setAgents((prev) => ({
      ...prev,
      [msg.agent]: msg.content,
    }));
  };

  const { connect } = useAgentSocket(handleMessage);

  const handleRun = (task) => {
    setAgents({});
    setFinalAnswer("");
    setLoading(true);
    connect(task);
  };

  return (
    <div style={{ maxWidth: "900px", margin: "auto", padding: "20px" }}>
      <h1>Multi-Agent AI System</h1>

      <PromptBox onSubmit={handleRun} loading={loading} />

      {finalAnswer && (
        <FinalOutput content={finalAnswer} />
      )}

      <div style={{ marginTop: "20px" }}>
        {Object.entries(agents).map(([agent, content]) => (
          <AgentPanel
            key={agent}
            agent={agent}
            content={content}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
