import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [to, setTo] = useState("");
  const [context, setContext] = useState("");
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [sent, setSent] = useState(false);
  const [error, setError] = useState("");

  const generatePreview = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setSent(false);

    try {
      const res = await axios.post("http://127.0.0.1:8000/agent/preview-email", {
        to,
        context,
      });

      setPreview(res.data);
    } catch (err) {
      setError("Failed to generate preview.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const confirmSend = async () => {
    setLoading(true);
    setError("");

    try {
      const res = await axios.post("http://127.0.0.1:8000/agent/confirm-send", {
        to: preview.to,
        subject: preview.subject,
        body: preview.body,
      });

      setSent(true);
      console.log(res.data);
    } catch (err) {
      setError("Failed to send email.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <div className="card">
        <h1>📧 AI Email Agent</h1>
        <p className="subtitle">
          Generate, preview & send emails using Groq + MCP + Gmail
        </p>

        <form onSubmit={generatePreview}>
          <label> Destination Email(s)</label>
          <input
            type="text"
            placeholder="person1@gmail.com, person2@gmail.com"
            value={to}
            onChange={(e) => setTo(e.target.value)}
            required
          />

          <label>Email Context</label>
          <textarea
            placeholder="Example: Ask politely about onboarding update..."
            value={context}
            onChange={(e) => setContext(e.target.value)}
            required
          />

          <button type="submit" disabled={loading}>
            {loading ? "Generating..." : "Generate Preview"}
          </button>
        </form>

        {error && <p className="error">{error}</p>}

        {preview && (
          <div className="result">
            <h3>Email Preview</h3>
            <p><strong>To:</strong> {preview.to}</p>
            <p><strong>Subject:</strong> {preview.subject}</p>
            <p><strong>Body:</strong></p>
            <pre>{preview.body}</pre>

            <button onClick={confirmSend} disabled={loading}>
              {loading ? "Sending..." : "Confirm Send"}
            </button>
          </div>
        )}

        {sent && <p className="success">Email sent successfully ✅</p>}
      </div>
    </div>
  );
}

export default App;