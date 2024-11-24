from app import db
from app.models.associations import workout_exercise

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    # Many-to-many relationship with Exercise
    exercises = db.relationship('Exercise', secondary=workout_exercise, back_populates='workouts')

    def __repr__(self):
        return f"<Workout {self.name}>"

