from app.extensions import db
from app.models.associations import workout_exercise
from sqlalchemy.types import JSON

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(50), nullable=False)
    muscle_groups = db.Column(JSON, nullable=False)
    needs_additional_weight = db.Column(db.Boolean, nullable=False)

    # Many-to-many relationship with Workout
    workouts = db.relationship('Workout', secondary=workout_exercise, back_populates='exercises')

    def __repr__(self):
        return f"<Exercise {self.name}>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'difficulty': self.difficulty,
            'muscle_groups': self.muscle_groups,
            'needs_additional_weight': self.needs_additional_weight
        }