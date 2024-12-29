from app import db
from app.models.basemodel import BaseModel


class Exercise(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(50), nullable=False)
    needs_additional_weight = db.Column(db.Boolean, nullable=False)

    # Many-to-many relationship with Workout
    workouts = db.relationship('Workout', secondary='workout_exercise', back_populates='exercises')
    muscle_groups = db.relationship('MuscleGroup', secondary='exercise_muscle_group',
                                    back_populates='exercises')

    def __repr__(self):
        return f"<Exercise {self.name}>"


    @staticmethod
    def search_by_name(name):
        exercises = Exercise.query.filter(Exercise.name.ilike(f'{name}%')).all()
        return exercises
