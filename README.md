# FluencyForge

FluencyForge is an event-driven spaced repetition backend built with:

- **SQL Server** (fact + dimension modeling)
- **Python ETL** (Obsidian ingestion)
- **FastAPI**

It tracks flashcard review behavior, maintains adaptive scheduling state, and preserves full historical review events for analytical insights.

---

## 🧠 Core Idea

The system separates:

- **Current scheduling state** (`cards`)
- **Historical review events** (`review_events`)

This enables:

- Adaptive interval calculation (SM-2 inspired)
- Ease factor mutation per card
- Full behavioral history tracking
- Analytics-ready data modeling

The database acts as the scheduling authority.

---

## 🚀 Current Features

- Markdown → SQL ETL pipeline
- Cleaned semantic text ingestion
- `GET /cards/new`
- `GET /cards/due`
- `POST /review/{card_id}`
- Adaptive interval updates
- Historical review logging
- Star-style schema design

---

## 🎯 Goal

FluencyForge is designed as a learning analytics engine rather than a simple flashcard app — prioritizing behavioral tracking, state/event separation, and extensibility.
