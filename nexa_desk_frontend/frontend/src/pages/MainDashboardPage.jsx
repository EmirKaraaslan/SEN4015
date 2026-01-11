import TopBar from "../components/stables/topBar";

import LandingCards from "../components/LandingCard";

function MainDashboardPage() {
  return (


    <div className="app-root">
      <TopBar />

      
        
        <div className="app-content">
          <LandingCards />
        </div>
      
    </div>
  );
}

export default MainDashboardPage;
