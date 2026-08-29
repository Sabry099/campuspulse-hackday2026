# CampusPulse

A personalized campus info dashboard — pulls course deadlines, club events, and scholarship
opportunities into one place so students stop missing things buried across scattered platforms.

Built for MMU Hack Day 2026.

## Project structure

```
campuspulse-starter/
├── backend/
│   ├── main.py           # FastAPI app + SQLite database + endpoints
│   └── requirements.txt
└── frontend/
    └── index.html        # Dashboard UI (vanilla HTML/CSS/JS, no build step needed)
```

## Running the backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

- API runs at `http://localhost:8000`
- Interactive docs (test endpoints in browser): `http://localhost:8000/docs`
- A `campuspulse.db` SQLite file is created automatically with 8 sample events on first run

### Endpoints
| Endpoint | Description |
|---|---|
| `GET /events` | All events, sorted by deadline |
| `GET /events?tag=CS` | Filter events by tag |
| `GET /digest?days=3` | Events due within N days (default 3) |
| `GET /tags` | List of distinct tags (for building filter dropdowns) |

## Running the frontend

No build step — just open `frontend/index.html` directly in a browser, or serve it:

```bash
cd frontend
python -m http.server 5500
```

Then visit `http://localhost:5500`. Make sure the backend is running first — the frontend
fetches from `http://localhost:8000` (see `API_BASE` at the top of the `<script>` in index.html).

## Next steps / ideas to extend

- Add a `users` table + simple interest-based filtering (match user interests to event tags)
- Add a calendar view instead of/alongside the card grid
- Add a "mark as done" or "dismiss" action per event
- Deploy: backend to Render/Railway (free tier), frontend to GitHub Pages or Vercel

## Team

Add your team members' names/roles here.
