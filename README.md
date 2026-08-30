# CampusPulse

**One place for everything at MMU.** CampusPulse pulls the announcements,
club events, scholarships and deadlines that are normally scattered across the
MMU portal, email and club chats into a single student dashboard.

Built for **MMU Hack Day 2026** by **Team Nexora**.

---

## The problem

Students miss announcements, deadlines, club events and scholarship
opportunities because the information is spread across too many platforms.
By the time you've checked the portal, your email, and three WhatsApp groups,
you've already missed something.

## What CampusPulse does

- **Unified dashboard** — services, announcements, club events and a deadline
  calendar in one place, organised as tabs.
- **Announcements feed** — campus notices with clear categories (urgent,
  notice, event, general) so the important ones stand out.
- **Club events** — upcoming events with date, time and location at a glance.
- **Deadline calendar** — an interactive month/week/day calendar (powered by
  FullCalendar) where you can add and remove your own deadlines.
- **Quick service launcher** — one-click access to eBwise, CLiC, Attendance,
  Finance and Scholarship pages, with search.

---

## Tech stack

- HTML, CSS, vanilla JavaScript (no build step)
- [FullCalendar](https://fullcalendar.io/) for the deadline calendar
- Google Fonts (Inter) and Font Awesome for UI

No framework, no server — it runs by opening a file in the browser.

---

## Run it locally

Clone the repo and open the login page in any browser:

```bash
git clone https://github.com/<your-username>/campuspulse.git
cd campuspulse
```

Then open `login.html` (double-click it, or use a local server):

```bash
# optional: serve it so relative links behave like a real site
python3 -m http.server 8000
# then visit http://localhost:8000/login.html
```

From the login screen, click **Continue to CampusPulse** to open the dashboard.

---

## Project structure

```
campuspulse/
├── login.html    # demo entry screen → opens the dashboard
├── index.html    # main dashboard (tabs: services, announcements, events, deadlines)
└── README.md
```

---

## Notes on the demo

This is a hackathon prototype, so a few things are worth stating plainly:

- **The login is a demo gate.** It does **not** collect MMU credentials and
  does not connect to any real login system. It starts a local demo session
  and opens the dashboard.
- **The service links are real** MMU URLs (eBwise, CLiC, etc.).
- **Announcements, club events and scholarships are sample data** for the
  demo. The architecture is built to be fed from a real MMU portal source;
  wiring that in is the natural next step.

---

## Roadmap

- Ingest live announcements from the MMU Online Portal
- Personalised ranking by faculty, campus and interests
- Notifications and a daily digest
- Real club-event and scholarship feeds

---

## Team

**Nexora** — MMU Hack Day 2026.
