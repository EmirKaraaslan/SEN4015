
import TopBar from "../components/stables/topBar";
import Sidebar from "../components/stables/sidebar.jsx";
import SoftwareTicketsCard from "../components/SoftwareTicketsDashBoard";

function SoftwarePage() {
  return (
    <div className="app-root">
      <TopBar />

      <div className="app-body">
        <Sidebar />
        <div className="app-content">
          <SoftwareTicketsCard />
        </div>
      </div>
    </div>
  );
}

export default SoftwarePage;
