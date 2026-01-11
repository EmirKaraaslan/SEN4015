import { useEffect, useMemo, useState } from "react";
import axios from "axios";
import "../styles/AllTicketsDB.scss";

const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

function toDateOnly(value) {
  if (!value) return "";
  const s = String(value);
  return s.includes("T") ? s.split("T")[0] : s.slice(0, 10);
}

function normalizeEnum(v) {
  if (!v) return "";
  return typeof v === "string" ? v : v.value || String(v);
}

function mapApiTicket(t) {
  return {
    id: t.ticket_number || t.ticket_id,
    ticket_id: t.ticket_id,
    ticket_number: t.ticket_number,
    title: t.title,
    description: t.description,
    category: normalizeEnum(t.category),
    priority: normalizeEnum(t.priority),
    status: normalizeEnum(t.status),
    createdAt: toDateOnly(t.created_at),
    updatedAt: toDateOnly(t.created_at),
    owner_id: t.owner_id,
  };
}

function AllTicketsCard() {
  const [tickets, setTickets] = useState([]);
  const [loading, setLoading] = useState(false);
  const [fetchError, setFetchError] = useState("");

  const [selectedTicket, setSelectedTicket] = useState(null);
  const [closing, setClosing] = useState(false);

  const user = useMemo(() => {
    try {
      return JSON.parse(localStorage.getItem("user") || "null");
    } catch {
      return null;
    }
  }, []);

  const userId = user?.user_id;
  const userRole = String(user?.role || "").toLowerCase();

  const fetchTickets = async () => {
    if (!userId) {
      setFetchError("No user session found. Please login again.");
      return;
    }

 
    if (userRole !== "admin") {
      setFetchError("Admin permission required to view all tickets.");
      return;
    }

    try {
      setLoading(true);
      setFetchError("");

    
      const res = await axios.get(`${API_BASE}/tickets/getAllTickets`, {
        params: { admin_id: userId },
      });

      setTickets((res.data || []).map(mapApiTicket));
    } catch (err) {
      const detail = err?.response?.data?.detail;
      setFetchError(detail || "Failed to load tickets.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTickets();
   
  }, [userId, userRole]);

  const handleRowClick = (ticket) => setSelectedTicket(ticket);
  const closeModal = () => setSelectedTicket(null);


  const handleCloseTicket = async () => {
    if (!selectedTicket) return;

    if (userRole !== "admin") {
      setFetchError("Admin permission required for this operation.");
      return;
    }

    const ticketId = selectedTicket.ticket_id;
    if (!ticketId) {
      setFetchError("ticket_id is missing. Cannot close ticket.");
      return;
    }

    try {
      setClosing(true);
      setFetchError("");

      const res = await axios.put(
        `${API_BASE}/tickets/closeTicket/${ticketId}`,
        { admin_id: userId },
        { headers: { "Content-Type": "application/json" } }
      );

      const updated = mapApiTicket(res.data);

      setTickets((prev) =>
        prev.map((t) => (t.ticket_id === updated.ticket_id ? updated : t))
      );

      setSelectedTicket(updated);
    } catch (err) {
      const detail = err?.response?.data?.detail;
      setFetchError(detail || "Failed to close ticket.");
    } finally {
      setClosing(false);
    }
  };

  const isClosableStatus = selectedTicket && selectedTicket.status === "Pending";
  const canClose = userRole === "admin" && isClosableStatus;

  return (
    <>
      <div className="hardware-card">
        {/* Header */}
        <div className="hardware-card__header">
          <div>
            <h1 className="hardware-card__title">All Tickets</h1>
            <p className="hardware-card__subtitle">
              Admin view: list and close any ticket in the system.
            </p>
          </div>
        </div>

        {/* Actions */}
        <div className="hardware-card__actions">
          <button
            type="button"
            className="hardware-card__create-button"
            onClick={fetchTickets}
            disabled={loading || userRole !== "admin"}
            title={userRole !== "admin" ? "Admin only" : "Refresh"}
          >
            ⟳ Refresh
          </button>

          <div className="hardware-card__legend">
            <span className="legend-dot legend-dot--open" /> Open
            <span className="legend-dot legend-dot--progress" /> Pending
            <span className="legend-dot legend-dot--resolved" /> Closed
          </div>
        </div>

        {/* Fetch states */}
        {loading && <div className="tickets-list__empty">Loading...</div>}
        {fetchError && <div className="tickets-list__empty">{fetchError}</div>}

        {/* Ticket list */}
        <div className="hardware-card__list">
          <div className="tickets-list__header">
            <span>ID</span>
            <span>Description</span>
            <span>Category</span>
            <span>Priority</span>
            <span>Status</span>
            <span>Updated</span>
          </div>

          <div className="tickets-list__body">
            {!loading &&
              !fetchError &&
              tickets.map((ticket) => (
                <div
                  className="tickets-list__row"
                  key={ticket.ticket_id}
                  onClick={() => handleRowClick(ticket)}
                >
                  <span className="tickets-list__cell tickets-list__cell--muted">
                    {ticket.id}
                  </span>
                  <span className="tickets-list__cell tickets-list__cell--title">
                    {ticket.title}
                  </span>
                  <span className="tickets-list__cell">{ticket.category}</span>
                  <span className="tickets-list__cell">
                    <span
                      className={`badge badge--priority-${String(ticket.priority).toLowerCase()}`}
                    >
                      {ticket.priority}
                    </span>
                  </span>
                  <span className="tickets-list__cell">
                    <span
                      className={`badge badge--status-${String(ticket.status)
                        .toLowerCase()
                        .replace(" ", "-")}`}
                    >
                      {ticket.status}
                    </span>
                  </span>
                  <span className="tickets-list__cell tickets-list__cell--muted">
                    {ticket.updatedAt}
                  </span>
                </div>
              ))}

            {!loading && !fetchError && tickets.length === 0 && (
              <div className="tickets-list__empty">No tickets found.</div>
            )}
          </div>
        </div>
      </div>

      {/* Ticket detail modal */}
      {selectedTicket && (
        <div className="ticket-modal__backdrop" onClick={closeModal}>
          <div className="ticket-modal" onClick={(e) => e.stopPropagation()}>
            <div className="ticket-modal__header">
              <div>
                <p className="ticket-modal__id">{selectedTicket.id}</p>
                <h2 className="ticket-modal__title">{selectedTicket.title}</h2>
              </div>
              <button type="button" className="ticket-modal__close" onClick={closeModal}>
                ✕
              </button>
            </div>

            <div className="ticket-modal__body">
              <div className="ticket-modal__meta-grid">
                <div className="ticket-modal__meta-item">
                  <span className="ticket-modal__label">Category</span>
                  <span className="ticket-modal__value">{selectedTicket.category}</span>
                </div>

                <div className="ticket-modal__meta-item">
                  <span className="ticket-modal__label">Priority</span>
                  <span className="ticket-modal__value">
                    <span
                      className={`badge badge--priority-${String(
                        selectedTicket.priority
                      ).toLowerCase()}`}
                    >
                      {selectedTicket.priority}
                    </span>
                  </span>
                </div>

                <div className="ticket-modal__meta-item">
                  <span className="ticket-modal__label">Status</span>
                  <span className="ticket-modal__value">
                    <span
                      className={`badge badge--status-${String(selectedTicket.status)
                        .toLowerCase()
                        .replace(" ", "-")}`}
                    >
                      {selectedTicket.status}
                    </span>
                  </span>
                </div>

                <div className="ticket-modal__meta-item">
                  <span className="ticket-modal__label">Owner</span>
                  <span className="ticket-modal__value">{selectedTicket.owner_id}</span>
                </div>

                <div className="ticket-modal__meta-item">
                  <span className="ticket-modal__label">Created</span>
                  <span className="ticket-modal__value">{selectedTicket.createdAt}</span>
                </div>
              </div>

              <div className="ticket-modal__section">
                <span className="ticket-modal__label">Description</span>
                <p className="ticket-modal__description">
                  {selectedTicket.description || "No description provided."}
                </p>
              </div>

              {canClose && (
                <div className="ticket-modal__actions">
                  <button
                    type="button"
                    className="ticket-modal__close-ticket-button"
                    onClick={handleCloseTicket}
                    disabled={closing}
                  >
                    {closing ? "Closing..." : "Close ticket"}
                  </button>
                </div>
              )}

              {isClosableStatus && userRole !== "admin" && (
                <div className="ticket-modal__actions">
                  <p className="tickets-list__empty">Only admins can close tickets.</p>
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </>
  );
}

export default AllTicketsCard;
