import "./App.css";
import LoginCard from "./components/LoginCard";
import TopBar from "./components/stables/topBar";
import Sidebar from "./components/stables/sidebar.JSX";
import HardwareTicketsCard from "./components/HardwareTicketsDashBoard";
import SoftwareTicketsCard from "./components/SoftwareTicketsDashBoard";
import LandingPage from "./components/LandingPage";
import CommentsPage from "./pages/CommentsPages";


function App() {
  return (

    /*
        <div className="app-root">
      <TopBar />

      <div className="app-body">
        <Sidebar />
        <div className="app-content">
          <HardwareTicketsCard />
        </div>
      </div>
    </div>
    
    
    */

    <CommentsPage />



  );
}

export default App;
