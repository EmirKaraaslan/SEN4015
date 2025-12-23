// src/pages/DashboardPage.jsx
import TopBar from "../components/stables/topBar";
import Sidebar from "../components/stables/sidebar.jsx";
import NetworkTicketsCard from "../components/NetworkTicketsDashBoard";

function NetworkPage() {
  return (
    <div className="app-root">
      <TopBar />

      <div className="app-body">
        <Sidebar />
        <div className="app-content">
          <NetworkTicketsCard />
        </div>
      </div>
    </div>
  );
}

export default NetworkPage;
