# TaskFlow — Task Management REST API

**TaskFlow** is a backend application for managing personal tasks, built with Django REST Framework and PostgreSQL.

The project provides a RESTful API with JWT authentication, task management, filtering, searching, sorting, and pagination.

## Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **Simple JWT**
- **Git & GitHub**

## Features

- JWT-based authentication
- Create, retrieve, update, and delete tasks
- User-specific task ownership
- Task status management
- Task priority management
- Search tasks by title and description
- Filter tasks by status and priority
- Sort tasks by creation date and title
- Pagination (5 tasks per page)
- API testing

## Task Model

Each task contains:

| Field | Description |
|---|---|
| `id` | Unique task identifier |
| `title` | Task title |
| `description` | Task description |
| `status` | pending, in_progress, completed |
| `priority` | low, medium, high |
| `owner` | Task owner |
| `created_at` | Creation timestamp |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health/` | Health check |
| POST | `/api/token/` | Obtain JWT tokens |
| POST | `/api/token/refresh/` | Refresh access token |
| GET | `/api/tasks/` | Get user's tasks |
| POST | `/api/tasks/` | Create a task |
| GET | `/api/tasks/{id}/` | Retrieve a task |
| PUT | `/api/tasks/{id}/` | Update a task |
| PATCH | `/api/tasks/{id}/` | Partially update a task |
| DELETE | `/api/tasks/{id}/` | Delete a task |

### Query Parameters

The tasks endpoint supports:

- `search` — search by title or description
- `status` — filter by task status
- `priority` — filter by priority
- `ordering` — sort by `created_at`, `-created_at`, `title`, or `-title`
- `page` — select pagination page

Example:

`GET /api/tasks/?status=pending&priority=high&ordering=-created_at`

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Dautkhan/TaskFlow.git
cd TaskFlow
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=taskflow_db
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run database
