# 🧭 NexaDesk – IT Service Ticket Management System

NexaDesk is a full-stack **IT Service & Ticket Management System** inspired by enterprise tools like ServiceNow.  
It enables users to create and track support tickets while administrators manage, monitor, and close tickets through a role-based dashboard.

This project is designed as a **cloud-ready, production-oriented application** with a clean architecture and modern development practices.

---

## 🚀 Features

### User
- Secure login and session handling
- Create support tickets (Hardware / Software / Network)
- View and track **only owned tickets**
- Real-time ticket status updates

### Admin
- View **all tickets** in the system
- Close tickets (admin-only operation)
- Strict role-based authorization (backend enforced)

### Dashboard
- Category-based ticket pages
- Modal ticket detail view
- Dark-themed, responsive UI
- Instant UI updates after create / close actions

---

## 🧱 Tech Stack

### Backend
- **FastAPI (Python)**
- **MongoDB** (Motor – async driver)
- **Pydantic** (data validation)
- RESTful API design
- Role-based access control

### Frontend
- **React (Vite)**
- **SCSS Modules**
- **Axios** for API communication
- Component-driven dashboard layout

### DevOps & Cloud
- **Docker** (backend containerization)
- **AWS ECS (Fargate)** – backend deployment
- **AWS S3 + CloudFront** – frontend hosting
- **Route 53 + ACM** – domain & TLS (HTTPS)

---

## 📁 Project Structure

nexa_desk_backend/
├── app/
│ ├── main.py
│ ├── database.py
│ ├── config.py
│ ├── routers/
│ ├── models/
│ └── services/
├── requirements.txt
├── Dockerfile
└── .env

nexa_desk_frontend/
├── src/
│ ├── components/
│ ├── pages/
│ ├── styles/
│ ├── App.jsx
│ └── main.jsx
├── package.json
└── vite.config.js


---

## 🔌 API Overview

| Method | Endpoint | Description | Role |
|------|---------|------------|------|
| POST | `/auth/loginSystem` | User/Admin login | All |
| POST | `/tickets/createTicket` | Create ticket | User |
| GET | `/tickets/getCustomTickets` | User’s tickets | User |
| GET | `/tickets/getAllTickets` | List all tickets | Admin |
| PUT | `/tickets/closeTicket/{ticket_id}` | Close ticket | Admin |
| GET | `/health` | Health check | Public |

---

---
## ⚙️ Local Development

### Backend 
```bash
cd nexa_desk_backend
uvicorn app.main:app --reload

http://127.0.0.1:8000

http://127.0.0.1:8000/docs



## Frontend

 
cd nexa_desk_frontend
npm install
npm run dev

---
### Docker

cd SEN4015

docker compose build

docker compose up 




