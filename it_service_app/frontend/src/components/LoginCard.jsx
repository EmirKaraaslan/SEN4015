import { useState } from "react";
import "../styles/LoginCardStyles.scss"

function LoginCard() {
  const [form, setForm] = useState({
    email: "",
    password: "",
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({
      ...prev,
      [name]: value,
    }));
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

      // 🔥 Burayı sonra FastAPI login endpoint’inle bağlayacağız
      console.log("Sending login request with:", form);

      await new Promise((resolve) => setTimeout(resolve, 800));

      setSuccess("Login successful (fake). FastAPI ile bağlayınca gerçek olacak.");
    } catch (err) {
      console.error(err);
      setError("Something went wrong. Please try again.");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="login-card">
     
      <div  style={{flexDirection:"row", display:"flex", alignItems:"center", justifyContent:"center", gap:"10px", marginBottom:"3rem" }}>
                <img 
          src="\NexaDeskLogo.png" 
          alt="NexaDesk Logo" 
          className="topbar__logo-image" 
        />
         <h1 className="app-title" >NexaDesk</h1>
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
          <button
            type="submit"
            className="login-button"
            disabled={isSubmitting}
          >
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
