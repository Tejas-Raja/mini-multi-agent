export default function FinalOutput({ content }) {
  if (!content) return null;

  return (
    <div
      style={{
        border: "2px solid green",
        padding: "12px",
        marginTop: "20px",
        borderRadius: "8px",
        background: "#f6fff6",
      }}
    >
      <h2>Final Output</h2>
      <pre style={{ whiteSpace: "pre-wrap" }}>{content}</pre>
    </div>
  );
}
