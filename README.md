# IT Ticket Management System

A full-stack IT Ticket Management System developed using Python-based backend and frontend technologies.  
The application is fully containerized with Docker and orchestrated using Docker Compose, providing a modular, scalable, and reproducible deployment setup.

---

## 📌 Project Overview

This project implements a basic IT ticket management platform where users can create, view, and manage support tickets through a web-based interface. The system is designed with a clear separation between frontend and backend services and follows modern DevOps and containerization practices.

---

## 🧱 Architecture Overview

The system consists of the following components:

- **Backend Service**
  - Python-based web application (Django-based)
  - Provides RESTful API endpoints
  - Handles business logic and data processing
  - Communicates with MongoDB via an external connection

- **Frontend Service**
  - Python-rendered web interface (Django Templates)
  - Consumes backend APIs over HTTP
  - Responsive UI using Bootstrap

- **Database**
  - MongoDB
  - Hosted as an external service (not containerized)
  - Connected via secure connection string using environment variables

- **Orchestration**
  - Docker & Docker Compose
  - Multi-container setup for frontend and backend services

- **Version Control**
  - Git
  - Private GitHub repository

---

## 🐳 Containerization & Orchestration

Both frontend and backend services are containerized using Docker.  
Docker Compose is used to orchestrate the services, enabling:

- Single-command application startup
- Service isolation
- Internal networking between containers
- Environment consistency across development environments

The MongoDB database is intentionally excluded from the container stack and runs as an external managed service. This reflects real-world production practices and improves scalability and security.

---

## 🚀 Getting Started

### Prerequisites

- Docker
- Docker Compose
- Git

---

### Clone the Repository

```bash
git clone <private-repository-url>
cd it-ticket-system
