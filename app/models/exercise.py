from app.extensions import db
from app.models.associations import workout_exercise, exercise_muscle_group
from sqlalchemy.types import JSON

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(50), nullable=False)
    needs_additional_weight = db.Column(db.Boolean, nullable=False)

    # Many-to-many relationship with Workout
    workouts = db.relationship('Workout', secondary=workout_exercise, back_populates='exercises')
    muscle_groups = db.relationship('MuscleGroup', secondary=exercise_muscle_group,
                                    back_populates='exercises')

    def __repr__(self):
        return f"<Exercise {self.name}>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'difficulty': self.difficulty,
            'muscle_groups': [muscle_group.name for muscle_group in self.muscle_groups],
            'needs_additional_weight': self.needs_additional_weight
        }

    @staticmethod
    def search_by_name(name):
        exercises = Exercise.query.filter(Exercise.name.ilike(f'{name}%')).all()
        return exercises

    @staticmethod
    def get_all():
        exercises = Exercise.query.all()
        return exercises