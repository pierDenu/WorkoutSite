# WorkoutSite

A Flask web application for creating and managing workout plans.

## Features

- Browse and search exercises by name or muscle group
- Create custom workouts by combining exercises with sets, reps, and rest times
- Build weekly training plans by assigning workouts to specific days
- Drag-and-drop interface for plan editing

## Tech Stack

- **Backend:** Python, Flask, SQLAlchemy, Flask-Migrate
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript (Vanilla), Bootstrap

## Getting Started

1. Clone the repository and create a virtual environment:
   ```bash
   git clone https://github.com/pier-dune/WorkoutSite.git
   cd WorkoutSite
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and set a real SECRET_KEY
   ```

3. Apply database migrations:
   ```bash
   flask --app app.run db upgrade
   ```

4. Seed the database with exercises:
   ```bash
   python app/scripts/seed_exercises.py
   ```

5. Run the development server:
   ```bash
   python app/run.py
   ```

The app will be available at `http://localhost:5000`.
