import { useState } from "react";
import "../styles/CommentsPanelStyles.scss";

function CommentSubmit() {
  const [comment, setComment] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();

    const trimmed = comment.trim();
    if (!trimmed) return;

    // Sonra burada FastAPI POST /comment yapacağız
    console.log("Submitted comment:", trimmed);

    setSubmitted(true);
    setComment("");
  };

  return (
    <div className="comment-submit-card">
      <h1 className="comment-submit-title">Submit a Comment</h1>
      <p className="comment-submit-subtitle">
        Send feedback, additional notes, or details related to your requests.
      </p>

      {!submitted ? (
        <form className="comment-submit-form" onSubmit={handleSubmit}>
          <textarea
            className="comment-submit-textarea"
            placeholder="Write your message..."
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            rows={4}
          />

          <button
            type="submit"
            className="comment-submit-button"
            disabled={!comment.trim()}
          >
            Submit
          </button>
        </form>
      ) : (
        <div className="comment-submit-success">
          <span>✔ Your comment has been submitted.</span>
          <button
            className="comment-submit-reset"
            onClick={() => setSubmitted(false)}
          >
            Submit another comment
          </button>
        </div>
      )}
    </div>
  );
}

export default CommentSubmit;
