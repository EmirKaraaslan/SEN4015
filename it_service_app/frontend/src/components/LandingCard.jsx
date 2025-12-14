// src/components/MainDashboard.jsx
import "../styles/LandingPageStyles.scss";
import { useNavigate } from "react-router-dom";
function LandingCards() {

  

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

        const handleCommentsClick = () => { 
        navigate("/dashboard/Comments")
    }

  


  
 

  return (
    <div className="dashboard">
      <div className="dashboard__header">
        <h1 className="dashboard__title">IT Support Dashboard</h1>
        <p className="dashboard__subtitle">
          Choose a category to view or create tickets.
        </p>
      </div>

      <div className="dashboard__grid">
        {/* Hardware */}
        <button
          type="button"
          className="dash-card dash-card--hardware"
          onClick={handleHardwareClick}
        >
          <div className="dash-card__icon-circle">HW</div>
          <div className="dash-card__body">
            <h2 className="dash-card__title">Hardware</h2>
            <p className="dash-card__text">
              Laptops, monitors, peripherals, docking stations and more.
            </p>
            <div className="dash-card__meta">
              <span className="dash-card__badge dash-card__badge--primary">
                3 open tickets
              </span>
              <span className="dash-card__hint">
                View hardware tickets &rarr;
              </span>
            </div>
          </div>
        </button>

        {/* Software */}
        <button
          type="button"
          className="dash-card dash-card--software"
          onClick={handleSoftwareClick}
        >
          <div className="dash-card__icon-circle">SW</div>
          <div className="dash-card__body">
            <h2 className="dash-card__title">Software</h2>
            <p className="dash-card__text">
              Installed applications, licenses, updates and access issues.
            </p>
            <div className="dash-card__meta">
              <span className="dash-card__badge dash-card__badge--secondary">
                5 open tickets
              </span>
              <span className="dash-card__hint">
                View software tickets &rarr;
              </span>
            </div>
          </div>
        </button>

        {/* Network */}
        <button
          type="button"
          className="dash-card dash-card--network"
          onClick={handleNetworkClick}
        >
          <div className="dash-card__icon-circle">NW</div>
          <div className="dash-card__body">
            <h2 className="dash-card__title">Network</h2>
            <p className="dash-card__text">
              VPN, Wi-Fi, connectivity, printers and internal systems.
            </p>
            <div className="dash-card__meta">
              <span className="dash-card__badge dash-card__badge--neutral">
                1 incident
              </span>
              <span className="dash-card__hint">
                View network tickets &rarr;
              </span>
            </div>
          </div>
        </button>

{/* Comments */}
<button
  type="button"
  className="dash-card dash-card--comments"
  onClick={handleCommentsClick}
>
  <div className="dash-card__icon-circle">CM</div>
  <div className="dash-card__body">
    <h2 className="dash-card__title">Comments</h2>
    <p className="dash-card__text">
      Review feedback, internal notes or conversation logs.
    </p>
    <div className="dash-card__meta">
      <span className="dash-card__badge dash-card__badge--comments">
        New entries
      </span>
      <span className="dash-card__hint">
        Send comments &rarr;
      </span>
    </div>
  </div>
</button>




      </div>
    </div>
  );
}

export default LandingCards;
