import { useState } from "react";

export default function PromptBox({ onSubmit, loading }) {
  const [task, setTask] = useState("");

  return (
    <div style={{ marginBottom: "1rem" }}>
      <textarea
        rows={4}
        placeholder="Enter your task (e.g. Write a business plan)"
        value={task}
        onChange={(e) => setTask(e.target.value)}
        style={{ width: "100%", padding: "8px" }}
      />
      <button
        onClick={() => onSubmit(task)}
        disabled={loading || !task}
        style={{ marginTop: "8px" }}
      >
        {loading ? "Running agents..." : "Run Agents"}
      </button>
    </div>
  );
}
