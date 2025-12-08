import "../../styles/stablesStyles/TopBarStyles.scss";

function TopBar() {
  const handleLogout = () => {
    console.log("Logout clicked");
    // Sonra burada token temizleyip login sayfasına yönlendireceğiz
  };

  return (
    <header className="topbar">
      <div className="topbar__left">
        <img 
          src="\NexaDeskLogo.png" 
          alt="NexaDesk Logo" 
          className="topbar__logo-image" 
        />

        <div className="topbar__brand">
          <span className="topbar__brand-title">NexaDesk</span>
          <span className="topbar__brand-subtitle">
            Internal support portal
          </span>
        </div>
      </div>



      <div className="topbar__right">
        <span className="topbar__user">Signed in as you</span>
        <button
          type="button"
          className="topbar__logout-button"
          onClick={handleLogout}
        >
          Logout
        </button>
      </div>
    </header>
  );
}

export default TopBar;
