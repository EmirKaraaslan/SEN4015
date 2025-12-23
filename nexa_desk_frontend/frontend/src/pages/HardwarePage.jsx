// src/pages/DashboardPage.jsx
import TopBar from "../components/stables/topBar";
import Sidebar from "../components/stables/sidebar.jsx";
import HardwareTicketsCard from "../components/HardwareTicketsDashBoard";

function HardwarePage() {
  return (
    <div className="app-root">
      <TopBar />

      <div className="app-body">
        <Sidebar />
        <div className="app-content">
          <HardwareTicketsCard />
        </div>
      </div>
    </div>
  );
}

export default HardwarePage;
