from app.extensions import db

class MuscleGroup(db.Model):
    __tablename__ = 'muscle_groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    exercises = db.relationship('Exercise', secondary='exercise_muscle_group', back_populates='muscle_groups')

    def __repr__(self):
        return f"<MuscleGroup {self.name}>"

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

    @staticmethod
    def get_all():
        muscle_groups = MuscleGroup.query.all()
        return muscle_groups
from app.models.associations import exercise_muscle_group