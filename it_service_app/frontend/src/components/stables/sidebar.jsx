import "../../styles/stablesStyles/sidebarStyles.scss";
import { useNavigate } from "react-router-dom";


function Sidebar() {

    const navigate = useNavigate();


    const handleHardwareClick = () => { 
        navigate("/dashboard/HardwareTickets")
    }

        const handleSoftwareClick = () => { 
        navigate("/dashboard/SoftwareTickets")
    }


        const handleNetworkClick = () => { 
        navigate("/dashboard/NetworkTickets")
    }

            const handleDashboardkClick = () => { 
        navigate("/dashboard")
    }



  return (
    <aside className="sidebar">
      <div className="sidebar__section sidebar__section--top">
        <p className="sidebar__label">Overview</p>
        <button className="sidebar__item sidebar__item--muted"
          onClick={handleDashboardkClick}
        >
          Dashboard
        </button>
      </div>

      <div className="sidebar__section">
        <p className="sidebar__label">Ticket types</p>

        <button className="sidebar__item sidebar__item--active"
          onClick={handleHardwareClick}
        >
          <span className="sidebar__bullet sidebar__bullet--hardware" />
          Hardware
        </button>

        <button className="sidebar__item"
          onClick={handleSoftwareClick}
          >
          <span className="sidebar__bullet sidebar__bullet--software" />
          Software
        </button>

        <button className="sidebar__item"
          onClick={handleNetworkClick}
          >
          <span className="sidebar__bullet sidebar__bullet--network" />
          Network
        </button>
        
        <button className="sidebar__item">
          <span className="sidebar__bullet sidebar__bullet--comments" />
          Comments
        </button>
      </div>

      <div className="sidebar__section">
        <p className="sidebar__label">My area</p>

        <button className="sidebar__item">
          My tickets
        </button>

        <button className="sidebar__item">
          All Tickets
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
