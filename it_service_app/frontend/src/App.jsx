import "./App.css";
import LoginCard from "./components/LoginCard";
import TopBar from "./components/stables/topBar";
import Sidebar from "./components/stables/sidebar.JSX";
import HardwareTicketsCard from "./components/HardwareTicketsDashBoard";
import SoftwareTicketsCard from "./components/SoftwareTicketsDashBoard";
import LandingPage from "./components/LandingPage";
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

     <div className="app-root">
      <TopBar />
      <div className="app-content">
        <LandingPage />
      </div>
    </div>



  );
}

export default App;
