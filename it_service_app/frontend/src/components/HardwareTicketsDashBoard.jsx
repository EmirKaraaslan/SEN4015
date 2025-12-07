import { useState } from "react";
import "../styles/HardwareTicketsDB.scss";


const initialTickets = [
  {
    id: "HW-1024",
    title: "Laptop not powering on",
    category: "Laptop",
    priority: "High",
    status: "Open",
    createdAt: "2025-12-05",
    updatedAt: "2025-12-05",
  },
  {
    id: "HW-1023",
    title: "External monitor flickering",
    category: "Monitor",
    priority: "Medium",
    status: "In Progress",
    createdAt: "2025-12-03",
    updatedAt: "2025-12-04",
  },
  {
    id: "HW-1022",
    title: "USB hub not detected",
    category: "Peripheral",
    priority: "Low",
    status: "Resolved",
    createdAt: "2025-12-01",
    updatedAt: "2025-12-02",
  },
];

function HardwareTicketsCard() {
  const [tickets, setTickets] = useState(initialTickets);
  const [showCreate, setShowCreate] = useState(false);
  const [selectedTicket, setSelectedTicket] = useState(null); // modal seçili ticket
  const [form, setForm] = useState({
    title: "",
    category: "Laptop",
    priority: "Medium",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleCreate = (e) => {
    e.preventDefault();
    if (!form.title.trim()) return;

    const today = new Date().toISOString().slice(0, 10);

    const newTicket = {
      id: `HW-${Math.floor(Math.random() * 9000) + 1000}`,
      title: form.title.trim(),
      category: form.category,
      priority: form.priority,
      status: "Open",
      createdAt: today,
      updatedAt: today,
    };

    setTickets((prev) => [newTicket, ...prev]);
    setForm({
      title: "",
      category: "Laptop",
      priority: "Medium",
    });
    setShowCreate(false);
  };

  const handleRowClick = (ticket) => {
    setSelectedTicket(ticket);
  };

  const closeModal = () => {
    setSelectedTicket(null);
  };

  // 🔥 Admin gibi davranıp ticket'ı kapatan fonksiyon
  const handleCloseTicket = () => {
    if (!selectedTicket) return;

    const today = new Date().toISOString().slice(0, 10);

    // listeyi güncelle
    setTickets((prev) =>
      prev.map((t) =>
        t.id === selectedTicket.id
          ? { ...t, status: "Resolved", updatedAt: today }
          : t
      )
    );

    // modal içindeki ticket'ı da güncelle
    setSelectedTicket((prev) =>
      prev
        ? {
            ...prev,
            status: "Resolved",
            updatedAt: today,
          }
        : prev
    );
  };

  const isClosableStatus =
    selectedTicket &&
    (selectedTicket.status === "Open" || selectedTicket.status === "In Progress");

  return (
    <>
      <div className="hardware-card">
        {/* Header */}
        <div className="hardware-card__header">
          <div>
            <h1 className="hardware-card__title">Hardware Tickets</h1>
            <p className="hardware-card__subtitle">
              View and manage your hardware-related tickets.
            </p>
          </div>
        </div>

        {/* Actions */}
        <div className="hardware-card__actions">
          <button
            type="button"
            className="hardware-card__create-button"
            onClick={() => setShowCreate((prev) => !prev)}
          >
            + Create ticket
          </button>
          <div className="hardware-card__legend">
            <span className="legend-dot legend-dot--open" /> Open
            <span className="legend-dot legend-dot--progress" /> In Progress
            <span className="legend-dot legend-dot--resolved" /> Resolved
          </div>
        </div>

        {/* Create ticket form */}
        {showCreate && (
          <form className="hardware-card__create-form" onSubmit={handleCreate}>
            <div className="create-form__row">
              <div className="create-form__field">
                <label htmlFor="title">Title</label>
                <input
                  id="title"
                  name="title"
                  type="text"
                  placeholder="Short description (e.g. Laptop keyboard not working)"
                  value={form.title}
                  onChange={handleChange}
                />
              </div>
            </div>
            <div className="create-form__row">
              <div className="create-form__field">
                <label htmlFor="category">Category</label>
                <select
                  id="category"
                  name="category"
                  value={form.category}
                  onChange={handleChange}
                >
                  <option value="Laptop">Laptop</option>
                  <option value="Monitor">Monitor</option>
                  <option value="Peripheral">Peripheral</option>
                  <option value="Network">Network</option>
                  <option value="Other">Other</option>
                </select>
              </div>
              <div className="create-form__field">
                <label htmlFor="priority">Priority</label>
                <select
                  id="priority"
                  name="priority"
                  value={form.priority}
                  onChange={handleChange}
                >
                  <option value="Low">Low</option>
                  <option value="Medium">Medium</option>
                  <option value="High">High</option>
                </select>
              </div>
              <div className="create-form__actions">
                <button
                  type="button"
                  className="secondary-button"
                  onClick={() => setShowCreate(false)}
                >
                  Cancel
                </button>
                <button type="submit" className="primary-button">
                  Create
                </button>
              </div>
            </div>
          </form>
        )}

        {/* Ticket list */}
        <div className="hardware-card__list">
          <div className="tickets-list__header">
            <span>ID</span>
            <span>Title</span>
            <span>Category</span>
            <span>Priority</span>
            <span>Status</span>
            <span>Updated</span>
          </div>

          <div className="tickets-list__body">
            {tickets.map((ticket) => (
              <div
                className="tickets-list__row"
                key={ticket.id}
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
                    className={`badge badge--priority-${ticket.priority.toLowerCase()}`}
                  >
                    {ticket.priority}
                  </span>
                </span>
                <span className="tickets-list__cell">
                  <span
                    className={`badge badge--status-${ticket.status
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

            {tickets.length === 0 && (
              <div className="tickets-list__empty">
                You don't have any hardware tickets yet. Create your first one.
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Ticket detail modal */}
      {selectedTicket && (
        <div className="ticket-modal__backdrop" onClick={closeModal}>
          <div
            className="ticket-modal"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="ticket-modal__header">
              <div>
                <p className="ticket-modal__id">{selectedTicket.id}</p>
                <h2 className="ticket-modal__title">
                  {selectedTicket.title}
                </h2>
              </div>
              <button
                type="button"
                className="ticket-modal__close"
                onClick={closeModal}
              >
                ✕
              </button>
            </div>

            <div className="ticket-modal__body">
              <div className="ticket-modal__meta-grid">
                <div className="ticket-modal__meta-item">
                  <span className="ticket-modal__label">Category</span>
                  <span className="ticket-modal__value">
                    {selectedTicket.category}
                  </span>
                </div>
                <div className="ticket-modal__meta-item">
                  <span className="ticket-modal__label">Priority</span>
                  <span className="ticket-modal__value">
                    <span
                      className={`badge badge--priority-${selectedTicket.priority.toLowerCase()}`}
                    >
                      {selectedTicket.priority}
                    </span>
                  </span>
                </div>
                <div className="ticket-modal__meta-item">
                  <span className="ticket-modal__label">Status</span>
                  <span className="ticket-modal__value">
                    <span
                      className={`badge badge--status-${selectedTicket.status
                        .toLowerCase()
                        .replace(" ", "-")}`}
                    >
                      {selectedTicket.status}
                    </span>
                  </span>
                </div>
                <div className="ticket-modal__meta-item">
                  <span className="ticket-modal__label">Created</span>
                  <span className="ticket-modal__value">
                    {selectedTicket.createdAt}
                  </span>
                </div>
                <div className="ticket-modal__meta-item">
                  <span className="ticket-modal__label">Last updated</span>
                  <span className="ticket-modal__value">
                    {selectedTicket.updatedAt}
                  </span>
                </div>
              </div>

              <div className="ticket-modal__section">
                <span className="ticket-modal__label">Description</span>
                <p className="ticket-modal__description">
                  No detailed description provided. In a real system, this area
                  would show the full problem description entered by the user.
                </p>
              </div>

              {/* 🔥 Admin close ticket action */}
              {isClosableStatus && (
                <div className="ticket-modal__actions">
                  <button
                    type="button"
                    className="ticket-modal__close-ticket-button"
                    onClick={handleCloseTicket}
                  >
                    Close ticket
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </>
  );
}

export default HardwareTicketsCard;
