import "../../styles/stablesStyles/sidebarStyles.scss";

function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar__section sidebar__section--top">
        <p className="sidebar__label">Overview</p>
        <button className="sidebar__item sidebar__item--muted">
          Dashboard
        </button>
      </div>

      <div className="sidebar__section">
        <p className="sidebar__label">Ticket types</p>

        <button className="sidebar__item sidebar__item--active">
          <span className="sidebar__bullet sidebar__bullet--hardware" />
          Hardware
        </button>

        <button className="sidebar__item">
          <span className="sidebar__bullet sidebar__bullet--software" />
          Software
        </button>

        <button className="sidebar__item">
          <span className="sidebar__bullet sidebar__bullet--network" />
          Network
        </button>
      </div>

      <div className="sidebar__section">
        <p className="sidebar__label">My area</p>

        <button className="sidebar__item">
          My tickets
        </button>

        <button className="sidebar__item">
          Approvals
        </button>
      </div>

      <div className="sidebar__section sidebar__section--bottom">
        <p className="sidebar__hint">
          Need help? <span>Contact IT</span>
        </p>
      </div>
    </aside>
  );
}

export default Sidebar;
