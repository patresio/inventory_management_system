<div align="center">

# 📦 SGE — Inventory Management System

**A production-ready inventory management system built with Django, featuring RESTful APIs, JWT authentication, and AI-powered analytics.**

<img src="https://github.com/patresio/sge-django-master/raw/master/.gitassets/capa.png" width="600" alt="SGE Dashboard" />

[![GitHub stars](https://img.shields.io/github/stars/patresio/sge-django-master?style=for-the-badge)](https://github.com/patresio/sge-django-master/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/patresio/sge-django-master?style=for-the-badge)](https://github.com/patresio/sge-django-master/network)
[![GitHub issues](https://img.shields.io/github/issues/patresio/sge-django-master?style=for-the-badge)](https://github.com/patresio/sge-django-master/issues)

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

</div>

---

## 🎯 Overview

**SGE (Sistema de Gestão de Estoque)** is a full-stack web application designed for **enterprise inventory management**. It provides complete product control, stock movement tracking, supplier management, and intelligent analytics through AI integration.

### Key Highlights

- **Clean Architecture** — Modular Django apps with clear separation of concerns
- **REST API** — Full-featured API with Django REST Framework and JWT authentication
- **AI Integration** — Google Gemini-powered insights and analytics
- **Production Ready** — Docker support, environment configuration, PostgreSQL

---

## 💼 Skills Demonstrated

> This project showcases proficiency in the following areas:

| Area | Technologies & Practices |
|------|--------------------------|
| **Backend Development** | Django 4.x, Python 3.10+, Class-Based Views (CBVs) |
| **API Design** | Django REST Framework, JWT Authentication, Serializers |
| **Database** | PostgreSQL, Django ORM, Relational Modeling, Migrations |
| **AI/ML Integration** | Google Gemini API, Prompt Engineering, Data Analysis |
| **DevOps** | Docker, Docker Compose, Environment Management |
| **Software Architecture** | Modular Apps, Django Signals, Service Layer Pattern |
| **Security** | User Authentication, Permission-based Access Control |

---

## ✨ Features

### Core Modules

| Module | Description |
|--------|-------------|
| **Products** | Complete CRUD with cost price, sale price, serial numbers, and quantity tracking |
| **Categories** | Hierarchical product organization |
| **Brands** | Manufacturer and brand management |
| **Suppliers** | Supplier registration with contact information |

### Stock Control

| Feature | Description |
|---------|-------------|
| **Inflows** | Purchase registration linked to suppliers and products |
| **Outflows** | Sales/withdrawals with automatic quantity updates |
| **Traceability** | Complete movement history with timestamps |

### Analytics Dashboard

- **Product Metrics** — Total inventory, stock value, category distribution
- **Sales Metrics** — Daily revenue, quantities sold
- **Interactive Charts** — Category and brand distribution visualizations
- **AI Insights** — Automated analysis powered by Google Gemini

---

## 🤖 AI Integration

The system includes an intelligent agent (`SGEAgent`) that leverages **Google Gemini** to provide:

```python
# AI Agent Architecture
class SGEAgent:
    def __init__(self):
        self.__client = settings.GOOGLE_API_KEY
        genai.configure(api_key=self.__client)

    def invoke(self):
        model = genai.GenerativeModel(
            model_name=settings.GOOGLE_MODEL_ID,
            system_instruction=SYSTEM_PROMPT
        )
        # Analyzes products and sales data
        # Generates actionable business insights
```

**Capabilities:**
- Analyzes product inventory and sales patterns
- Generates business insights and recommendations
- Stores AI-generated results for dashboard visualization

---

## 🏗️ Architecture

```
sge-django-master/
├── core/               # Django settings, URLs, WSGI configuration
├── authentication/     # User authentication system
├── dashboard/          # Main dashboard with metrics and charts
├── products/           # Product management module
├── brands/             # Brand management module
├── categories/         # Category management module
├── suppliers/          # Supplier management module
├── inflows/            # Stock entry management (with Django Signals)
├── outflows/           # Stock exit management (with Django Signals)
├── api/                # REST API endpoints (Django REST Framework)
├── ai/                 # Google Gemini AI integration
├── services/           # External services layer
├── utils/              # Helper functions and utilities
└── templates/          # HTML templates (Bootstrap 5)
```

### Design Patterns & Best Practices

- **Django Signals** — Automatic stock quantity updates on inflow/outflow operations
- **Class-Based Views** — Consistent CRUD operations across all modules
- **Generic API Views** — `ListCreateAPIView`, `RetrieveDestroyAPIView` for REST endpoints
- **Service Layer** — Separation of external service integrations
- **Environment Configuration** — Secure credential management with `python-decouple`

---

## 🔌 REST API

Full RESTful API with JWT authentication:

```
Authentication:
POST   /api/token/           # Obtain JWT token
POST   /api/token/refresh/   # Refresh token

Resources:
GET/POST    /api/products/
GET/DELETE  /api/products/<id>/
GET/POST    /api/brands/
GET/POST    /api/categories/
GET/POST    /api/suppliers/
GET/POST    /api/inflows/
GET/POST    /api/outflows/
```

---

## 🛠️ Tech Stack

<table>
<tr>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="48" height="48" alt="Python" />
<br>Python
</td>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="48" height="48" alt="Django" />
<br>Django
</td>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="48" height="48" alt="PostgreSQL" />
<br>PostgreSQL
</td>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="48" height="48" alt="Docker" />
<br>Docker
</td>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" width="48" height="48" alt="Bootstrap" />
<br>Bootstrap
</td>
</tr>
</table>

### Dependencies

| Package | Purpose |
|---------|---------|
| `django` | Core web framework |
| `djangorestframework` | REST API development |
| `djangorestframework-simplejwt` | JWT authentication |
| `google-generativeai` | Gemini AI integration |
| `python-decouple` | Environment variable management |
| `dj-database-url` | Database URL configuration |

---

## ⚙️ Environment Variables

Create a `.env` file with the following configuration:

```env
# Django Settings
SECRET_KEY=your-secret-key
DEBUG=True

# Database
DATABASE_URL=postgres://user:password@localhost:5432/sge_db

# Google AI (Gemini)
GOOGLE_API_KEY=your-google-api-key
GOOGLE_MODEL_ID=gemini-pro
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- PostgreSQL (or SQLite for development)
- Docker & Docker Compose (optional)

### 🐳 Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/patresio/sge-django-master.git
cd sge-django-master

# Start with Docker Compose
docker-compose up -d

# Access: http://localhost:8000
```

### 🐍 Local Installation

```bash
# Clone repository
git clone https://github.com/patresio/sge-django-master.git
cd sge-django-master

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env  # Edit with your credentials

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver

# Access: http://localhost:8000
```

---

## 📸 Screenshots

<div align="center">

![Dashboard](https://github.com/patresio/sge-django-master/raw/master/.gitassets/2.jpg)
*Dashboard with real-time metrics and interactive charts*

</div>

---

## 🗺️ Roadmap

- [ ] Unit and Integration Tests with `pytest`
- [ ] API Documentation with Swagger/OpenAPI
- [ ] Kubernetes deployment configuration
- [ ] Advanced AI analytics with trend prediction
- [ ] Multi-tenant support

---

## 📄 License

This project was developed for educational purposes and technical skill demonstration.

---

## 👤 Author

Developed by **[@patresio](https://github.com/patresio)**

<div align="center">

⭐ **If you found this project useful, consider giving it a star!** ⭐

</div>