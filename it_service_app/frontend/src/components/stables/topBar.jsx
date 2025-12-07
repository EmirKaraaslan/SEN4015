import "../../styles/stablesStyles/TopBarStyles.scss";

function TopBar() {
  const handleLogout = () => {
    console.log("Logout clicked");
    // Sonra burada token temizleyip login sayfasına yönlendireceğiz
  };

  return (
    <header className="topbar">
      <div className="topbar__left">
        <div className="topbar__logo-circle">IT</div>
        <div className="topbar__brand">
          <span className="topbar__brand-title">IT Service Desk</span>
          <span className="topbar__brand-subtitle">
            Internal support portal
          </span>
        </div>
      </div>

      <nav className="topbar__nav">
        <button className="topbar__nav-item topbar__nav-item--active">
          Hardware
        </button>
        <button className="topbar__nav-item">Software</button>
        <button className="topbar__nav-item">Network</button>
      </nav>

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
