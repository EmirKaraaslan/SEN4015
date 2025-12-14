// src/App.jsx
import { Routes, Route } from "react-router-dom";
import LoginPage  from "../src/pages/LoginPage"
import MainDashboardPage from "./pages/MainDashboardPage";
import HardwarePage from "./pages/HardwarePage";
import SoftwarePage from "./pages/SoftwarePages";
import NetworkPage from "./pages/NetworkPages";
import CommentsPage from "./pages/CommentsPages";

function App() {
  return (
    <div className="app-root">
    <Routes>
      {/* Login ekranı */}
      <Route path="/" element={<LoginPage />} />

      {/* Dashboard ekranı */}
      <Route path="/dashboard" element={<MainDashboardPage />} />

      {/* Hardware Ticketlarının olduğu ekran */}
      <Route path="/dashboard/HardwareTickets" element={<HardwarePage/>} />

      {/* Software Ticketlarının olduğu ekran */}
      <Route path="/dashboard/SoftwareTickets" element={<SoftwarePage/>} />

      {/* Network Ticketlarının olduğu ekran */}
      <Route path="/dashboard/NetworkTickets" element={<NetworkPage/>} />

      {/* Comments Ticketlarının olduğu ekran */}
      <Route path="/dashboard/Comments" element={<CommentsPage/>} />


    </Routes>

    </div>

  );
}

export default App;
