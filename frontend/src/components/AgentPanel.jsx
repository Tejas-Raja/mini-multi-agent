export default function AgentPanel({ agent, content }) {
  return (
    <div
      style={{
        border: "1px solid #ddd",
        padding: "10px",
        marginBottom: "10px",
        borderRadius: "6px",
      }}
    >
      <h3>{agent}</h3>
      <pre style={{ whiteSpace: "pre-wrap" }}>{content}</pre>
    </div>
  );
}
