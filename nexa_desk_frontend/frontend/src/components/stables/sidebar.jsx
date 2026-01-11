import "../../styles/stablesStyles/sidebarStyles.scss";
import { useNavigate, useLocation } from "react-router-dom";
import { useMemo } from "react";

function Sidebar() {
  const navigate = useNavigate();
  const location = useLocation();

  const currentPath = location.pathname.toLowerCase();
  const isActive = (path) => currentPath.includes(path.toLowerCase());

  
  const user = useMemo(() => {
    try {
      return JSON.parse(localStorage.getItem("user") || "null");
    } catch {
      return null;
    }
  }, []);

  const isAdmin = String(user?.role || "").toLowerCase() === "admin";

  return (
    <aside className="sidebar">
      {}
      <div className="sidebar__section sidebar__section--top">
        <p className="sidebar__label">Overview</p>
        <button
          className={`sidebar__item ${
            isActive("/dashboard") &&
            !isActive("hardware") &&
            !isActive("software") &&
            !isActive("network") &&
            !isActive("comments")
              ? "sidebar__item--active"
              : "sidebar__item--muted"
          }`}
          onClick={() => navigate("/dashboard")}
        >
          Dashboard
        </button>
      </div>

      {}
      <div className="sidebar__section">
        <p className="sidebar__label">Ticket types</p>

        <button
          className={`sidebar__item ${
            isActive("/hardwaretickets") ? "sidebar__item--active" : ""
          }`}
          onClick={() => navigate("/dashboard/HardwareTickets")}
        >
          <span className="sidebar__bullet sidebar__bullet--hardware" />
          Hardware
        </button>

        <button
          className={`sidebar__item ${
            isActive("/softwaretickets") ? "sidebar__item--active" : ""
          }`}
          onClick={() => navigate("/dashboard/SoftwareTickets")}
        >
          <span className="sidebar__bullet sidebar__bullet--software" />
          Software
        </button>

        <button
          className={`sidebar__item ${
            isActive("/networktickets") ? "sidebar__item--active" : ""
          }`}
          onClick={() => navigate("/dashboard/NetworkTickets")}
        >
          <span className="sidebar__bullet sidebar__bullet--network" />
          Network
        </button>

        <button
          className={`sidebar__item ${
            isActive("/comments") ? "sidebar__item--active" : ""
          }`}
          onClick={() => navigate("/dashboard/Comments")}
        >
          <span className="sidebar__bullet sidebar__bullet--comments" />
          Comments
        </button>
      </div>

      {}
      {isAdmin && (
        <div className="sidebar__section">
          <p className="sidebar__label">My area</p>

          <button
            className={`sidebar__item ${
              isActive("/alltickets") ? "sidebar__item--active" : ""
            }`}
            onClick={() => navigate("/dashboard/AllTickets")}
          >
            All Tickets
          </button>
        </div>
      )}

      {}
      <div className="sidebar__section sidebar__section--bottom">
        <p className="sidebar__hint">
          Need help? <span>Contact IT</span>
        </p>
      </div>
    </aside>
  );
}

export default Sidebar;
