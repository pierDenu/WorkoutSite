from app import db
from .associations import workout_exercises  # Import the association table

class Workout(db.Model):
    __tablename__ = 'workout'  # Explicitly define the table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    muscle_group = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    # Many-to-many relationship with Exercise
    exercises = db.relationship('Exercise', secondary=workout_exercises, back_populates='workouts')

    def __repr__(self):
        return f"<Workout {self.name}>"
