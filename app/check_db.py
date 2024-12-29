from app import create_app, db
from app.models.muscle_group import MuscleGroup

app = create_app()

with app.app_context():
    muscle_groups = MuscleGroup.query.all()
    print(muscle_groups)
