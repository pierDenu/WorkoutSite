from app import create_app, db
from app.models.workout import Workout  # Import the models (Workout, Exercise, etc.)
from app.models.exercise import Exercise

# Create the Flask application
app = create_app()

# Create database tables (if they don't exist yet)
with app.app_context():
    db.create_all()  # Create all tables defined in your models

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
