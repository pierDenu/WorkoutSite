from app import db
from app.models.basemodel import BaseModel


class MuscleGroup(BaseModel):
    __tablename__ = 'muscle_group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    exercises = db.relationship('Exercise', secondary='exercise_muscle_group', back_populates='muscle_groups')

    def __repr__(self):
        return f"<MuscleGroup {self.name}>"

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

