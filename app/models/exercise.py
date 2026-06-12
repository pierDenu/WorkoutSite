from app import db
from app.models.basemodel import BaseModel


class Exercise(BaseModel):
    __tablename__ = 'exercise'
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


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'difficulty': self.difficulty,
            'needs_additional_weight': self.needs_additional_weight,
            'muscle_groups': [mg.name for mg in self.muscle_groups],
        }

    @staticmethod
    def search_by_name(name):
        return Exercise.query.filter(Exercise.name.ilike(f'{name}%')).all()
