// src/pages/DashboardPage.jsx
import TopBar from "../components/stables/topBar";
import Sidebar from "../components/stables/sidebar.jsx";
import AllTicketsCard from "../components/AllTicketsDashBoard";

function AllTicketsPage() {
  return (
    <div className="app-root">
      <TopBar />

      <div className="app-body">
        <Sidebar />
        <div className="app-content">
          <AllTicketsCard />
        </div>
      </div>
    </div>
  );
}

export default AllTicketsPage;
