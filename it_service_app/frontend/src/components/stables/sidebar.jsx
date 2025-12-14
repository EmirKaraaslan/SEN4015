import "../../styles/stablesStyles/sidebarStyles.scss";
import { useNavigate, useLocation } from "react-router-dom";

function Sidebar() {
  const navigate = useNavigate();
  const location = useLocation();

  // 🔥 Aktif route'ı kontrol et
  const currentPath = location.pathname.toLowerCase();

  const isActive = (path) => currentPath.includes(path.toLowerCase());

  const handleNavigate = (path) => navigate(path);

  return (
    <aside className="sidebar">
      {/* --- Overview --- */}
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
          onClick={() => handleNavigate("/dashboard")}
        >
          Dashboard
        </button>
      </div>

      {/* --- Ticket Types --- */}
      <div className="sidebar__section">
        <p className="sidebar__label">Ticket types</p>

        <button
          className={`sidebar__item ${
            isActive("/hardwaretickets") ? "sidebar__item--active" : ""
          }`}
          onClick={() => handleNavigate("/dashboard/HardwareTickets")}
        >
          <span className="sidebar__bullet sidebar__bullet--hardware" />
          Hardware
        </button>

        <button
          className={`sidebar__item ${
            isActive("/softwaretickets") ? "sidebar__item--active" : ""
          }`}
          onClick={() => handleNavigate("/dashboard/SoftwareTickets")}
        >
          <span className="sidebar__bullet sidebar__bullet--software" />
          Software
        </button>

        <button
          className={`sidebar__item ${
            isActive("/networktickets") ? "sidebar__item--active" : ""
          }`}
          onClick={() => handleNavigate("/dashboard/NetworkTickets")}
        >
          <span className="sidebar__bullet sidebar__bullet--network" />
          Network
        </button>

        <button
          className={`sidebar__item ${
            isActive("/comments") ? "sidebar__item--active" : ""
          }`}
          onClick={() => handleNavigate("/dashboard/Comments")}
        >
          <span className="sidebar__bullet sidebar__bullet--comments" />
          Comments
        </button>
      </div>

      {/* --- My Area --- */}
      <div className="sidebar__section">
        <p className="sidebar__label">My area</p>

        <button
          className={`sidebar__item ${
            isActive("/my-tickets") ? "sidebar__item--active" : ""
          }`}
          onClick={() => handleNavigate("/dashboard/MyTickets")}
        >
          My tickets
        </button>

        <button
          className={`sidebar__item ${
            isActive("/all-tickets") ? "sidebar__item--active" : ""
          }`}
          onClick={() => handleNavigate("/dashboard/AllTickets")}
        >
          All Tickets
        </button>
      </div>

      {/* --- Footer --- */}
      <div className="sidebar__section sidebar__section--bottom">
        <p className="sidebar__hint">
          Need help? <span>Contact IT</span>
        </p>
      </div>
    </aside>
  );
}

export default Sidebar;
