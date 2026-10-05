# Notes App

A full stack notes app with a FastAPI backend and a vanilla JavaScript frontend. Notes show up as cards you can edit in place, and everything saves automatically.



**Live demo:** https://silly-panda-c0fa09.netlify.app
**API docs:** https://notes-app-o8la.onrender.com/docs

> The API runs on a free hosting tier, so the first request after a quiet period can take around 30 seconds while the service wakes up.

## Features

- Full CRUD: create, read, update and delete notes
- Responsive card grid
- Inline editing with debounced auto-save (saves 2 seconds after you stop typing)
- Request validation with Pydantic and proper `404` responses for missing notes
- Containerized with Docker and deployed to the cloud

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, FastAPI, SQLAlchemy |
| Database | PostgreSQL (Supabase) |
| Frontend | HTML, CSS, vanilla JavaScript (`fetch`) |
| Containers | Docker, Docker Compose, nginx |
| Hosting | Render (API), Netlify (frontend) |

## Project Structure

```
NotesApp/
├── backend/
│   ├── app/
│   │   ├── main.py          # app setup, CORS, router registration
│   │   ├── database.py      # engine, session, Base, get_db dependency
│   │   ├── models.py        # SQLAlchemy Note model
│   │   ├── schemas.py       # Pydantic request and response models
│   │   ├── crud.py          # database operations
│   │   └── routers/
│   │       └── notes.py     # /notes endpoints
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── .env.example
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── index.js
│   ├── style.css
│   └── Dockerfile
├── docs/
│   └── screenshot.png
├── docker-compose.yml
├── LICENSE
└── README.md
```

## API Reference

Base path: `/notes`

| Method | Endpoint | Description | Success | Errors |
|--------|----------|-------------|---------|--------|
| `POST` | `/notes/` | Create a note | `201` | `422` invalid body |
| `GET` | `/notes/` | List all notes | `200` | |
| `GET` | `/notes/{id}` | Get one note | `200` | `404` not found |
| `PUT` | `/notes/{id}` | Update a note | `200` | `404`, `422` |
| `DELETE` | `/notes/{id}` | Delete a note | `204` | `404` not found |

Request body for `POST` and `PUT`:

```json
{
  "title": "Groceries",
  "content": "milk, eggs, bread"
}
```

Response body:

```json
{
  "id": 1,
  "title": "Groceries",
  "content": "milk, eggs, bread",
  "created_at": "2026-10-06T10:15:00Z",
  "edited_at": "2026-10-06T10:15:00Z"
}
```

You can also try every endpoint from the interactive docs at `/docs`.

## Getting Started

### Prerequisites

- Python 3.11 or newer
- A PostgreSQL database (a free Supabase project works fine)
- Docker Desktop (optional, for the containerized setup)

### 1. Clone the repo

```bash
git clone https://github.com/Prajit208/notes-app.git
cd notes-app
```

### 2. Set up environment variables

Copy the example file and fill in your own connection string:

```bash
cp backend/.env.example backend/.env
```

`backend/.env` should look like this:

```
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@HOST:5432/postgres
```

If your password has special characters, percent-encode them (for example `@` becomes `%40`). The real `.env` is git-ignored, so never commit it.

### 3. Run locally

Backend:

```bash
cd backend
python -m venv venv
source venv/Scripts/activate      # Windows Git Bash. On macOS/Linux use venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API is now at `http://127.0.0.1:8000` and the `notes` table is created automatically on startup.

Frontend: open `frontend/index.html` with a local server, for example the VS Code Live Server extension. It picks the API address on its own: `http://localhost:8000` when served from localhost, and the deployed API everywhere else.

### Run with Docker instead

```bash
docker compose up --build
```

- Frontend: `http://localhost`
- API: `http://localhost:8000`

Compose reads `DATABASE_URL` from `backend/.env`, so complete step 2 first.

## Deployment

- **Backend:** Render, as a Docker web service with `backend` as the root directory. `DATABASE_URL` and `PORT` are set as environment variables.
- **Frontend:** Netlify, with no build command and `frontend` as the publish directory.
- **CORS:** allowed origins are listed in `origins` in `backend/app/main.py`. If you fork this and host your own frontend, add your frontend URL there or the browser will block the requests.

## Known Limitations

- No authentication, so all notes are shared and visible to anyone with the URL.
- The schema is created with `create_all`, which does not alter existing tables. Schema changes will need a migration tool such as Alembic.

## Roadmap

- [ ] User accounts and per-user notes
- [ ] Search, pinning and tags
- [ ] Alembic migrations
- [ ] Tighter CORS configuration
- [ ] Automated tests

## License

Released under the MIT License. See [LICENSE](LICENSE) for details.

## Author

Built by Prajit. GitHub: [Prajit208](https://github.com/Prajit208)