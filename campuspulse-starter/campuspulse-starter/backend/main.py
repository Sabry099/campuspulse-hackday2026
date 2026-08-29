"""
CampusPulse backend — FastAPI + SQLite
Run with: uvicorn main:app --reload --port 8000
Docs available at: http://localhost:8000/docs
"""

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from datetime import date, timedelta
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "campuspulse.db")

app = FastAPI(title="CampusPulse API")

# Allow the frontend (running on a different port/file) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # fine for a hackathon demo; tighten for production
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            type TEXT NOT NULL,       -- 'course', 'club', or 'scholarship'
            tag TEXT NOT NULL,        -- e.g. 'CS', 'sports', 'finance'
            deadline TEXT NOT NULL,   -- ISO date string YYYY-MM-DD
            description TEXT
        )
    """)
    conn.commit()

    # Seed with sample data only if the table is empty
    count = conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
    if count == 0:
        today = date.today()
        sample_events = [
            ("Data Structures Assignment 2 Due", "course", "CS", str(today + timedelta(days=1)), "Submit via LMS before 11:59 PM"),
            ("Photography Club Meetup", "club", "arts", str(today + timedelta(days=2)), "Weekly meetup at FCI lobby"),
            ("Merit Scholarship Application Closes", "scholarship", "finance", str(today + timedelta(days=3)), "Apply via student portal"),
            ("Algorithm Design Group Project Milestone", "course", "CS", str(today), "Submit progress report"),
            ("Basketball Club Tryouts", "club", "sports", str(today + timedelta(days=5)), "Bring sports attire"),
            ("Statistics Quiz 3", "course", "math", str(today + timedelta(days=1)), "Covers chapters 5-7"),
            ("Entrepreneur Talk Series", "club", "business", str(today + timedelta(days=4)), "Guest speaker session"),
            ("Book Prize Scholarship Deadline", "scholarship", "finance", str(today + timedelta(days=7)), "GPA 3.5+ required"),
        ]
        conn.executemany(
            "INSERT INTO events (title, type, tag, deadline, description) VALUES (?, ?, ?, ?, ?)",
            sample_events,
        )
        conn.commit()
    conn.close()


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    return {"message": "CampusPulse API is running. See /docs for endpoints."}


@app.get("/events")
def get_events(tag: str = Query(None, description="Filter by tag, e.g. CS, sports, finance")):
    conn = get_db()
    if tag:
        rows = conn.execute(
            "SELECT * FROM events WHERE tag = ? ORDER BY deadline ASC", (tag,)
        ).fetchall()
    else:
        rows = conn.execute("SELECT * FROM events ORDER BY deadline ASC").fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.get("/digest")
def get_digest(days: int = Query(3, description="Show events due within this many days")):
    """Returns events happening soon — the 'today's digest' view."""
    conn = get_db()
    cutoff = str(date.today() + timedelta(days=days))
    rows = conn.execute(
        "SELECT * FROM events WHERE deadline <= ? ORDER BY deadline ASC", (cutoff,)
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.get("/tags")
def get_tags():
    """Returns the distinct tags available, useful for building a filter dropdown."""
    conn = get_db()
    rows = conn.execute("SELECT DISTINCT tag FROM events").fetchall()
    conn.close()
    return [row["tag"] for row in rows]
