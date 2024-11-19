from app import db
from associations import workout_exercises  # Import the association table

class Exercise(db.Model):
    __tablename__ = 'exercise'  # Explicitly define the table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    muscle_group = db.Column(db.String(100), nullable=False)
    need_additional_weight = db.Column(db.Boolean, nullable=False)

    # Many-to-many relationship with Workout
    workouts = db.relationship('Workout', secondary=workout_exercises, back_populates='exercises')

    def __repr__(self):
        return f"<Exercise {self.name}>"
