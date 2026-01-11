import { useState } from "react";
import "../styles/LoginCardStyles.scss";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

function LoginCard() {
  const [form, setForm] = useState({ email: "", password: "" });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
    setError("");
    setSuccess("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    if (!form.email || !form.password) {
      setError("Email and password are required.");
      return;
    }

    try {
      setIsSubmitting(true);

      const res = await axios.post(
        `${API_BASE}/auth/loginSystem`,
        {
          email: form.email,
          password: form.password,
        },
        {
          headers: { "Content-Type": "application/json" },
        }
      );

      
      const data = res.data;

      if (data?.success) {
        setSuccess(data.message || "Login successful!");
        
        localStorage.setItem("user", JSON.stringify(data.user));
        navigate("/dashboard");
      } else {
        setError(data?.message || "Login failed.");
      }
    } catch (err) {
      
      const detail = err?.response?.data?.detail;
      setError(detail || "Something went wrong. Please try again.");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="login-card">
      <div style={{flexDirection:"row", display:"flex", alignItems:"center", justifyContent:"center", gap:"10px", marginBottom:"3rem" }}>
        <img src="\NexaDeskLogo.png" alt="NexaDesk Logo" className="topbar__logo-image" />
        <h1 className="app-title">NexaDesk</h1>
      </div>

      <form onSubmit={handleSubmit} className="login-form">
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            id="email"
            name="email"
            type="email"
            placeholder="name.surname@company.com"
            value={form.email}
            onChange={handleChange}
            autoComplete="email"
          />
        </div>

        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            id="password"
            name="password"
            type="password"
            placeholder="••••••••"
            value={form.password}
            onChange={handleChange}
            autoComplete="current-password"
          />
        </div>

        <div className="form-footer">
          <div className="remember-me">
            <input id="remember" type="checkbox" />
            <label htmlFor="remember">Remember me</label>
          </div>

          <button type="submit" className="login-button" disabled={isSubmitting}>
            {isSubmitting ? "Signing in..." : "Sign in"}
          </button>
        </div>

        {error && <p className="message error">{error}</p>}
        {success && <p className="message success">{success}</p>}
      </form>

      <p className="help-text">
        Having trouble? <span>Contact IT Support</span>
      </p>
    </div>
  );
}

export default LoginCard;
