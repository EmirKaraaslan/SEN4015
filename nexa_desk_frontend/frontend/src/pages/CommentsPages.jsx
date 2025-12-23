// src/pages/DashboardPage.jsx
import TopBar from "../components/stables/topBar";
import Sidebar from "../components/stables/sidebar.jsx";
import CommentSubmit from "../components/CommentPanel";

function CommentsPage() {
  return (
    <div className="app-root">
      <TopBar />

      <div className="app-body">
        <Sidebar />
        <div className="app-content">
          <CommentSubmit />
        </div>
      </div>
    </div>
  );
}

export default CommentsPage;
