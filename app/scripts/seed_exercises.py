# seed_exercises.py
from app import db
from app.models.exercise import Exercise

# Sample exercises to add
exercises = [
    Exercise(name="Push-Ups", difficulty="Medium", muscle_groups=["Chest", "Triceps"], needs_additional_weight=False),
    Exercise(name="Dips", difficulty="Medium", muscle_groups=["Chest", "Triceps"], needs_additional_weight=False),
    Exercise(name="Weighted Dips", difficulty="Hard", muscle_groups=["Chest", "Triceps"], needs_additional_weight=True),
    Exercise(name="Pull-Ups", difficulty="Medium", muscle_groups=["Back", "Biceps"], needs_additional_weight=False),
    Exercise(name="Weighted Pull-Ups", difficulty="Hard", muscle_groups=["Back", "Biceps"], needs_additional_weight=True),
    Exercise(name="Pike Push-Ups", difficulty="Medium", muscle_groups=["Shoulders"], needs_additional_weight=False),
    Exercise(name="Handstand Push-Ups", difficulty="Hard", muscle_groups=["Shoulders"], needs_additional_weight=False),

]

# Add each exercise to the database session
with db.session.begin():
    db.session.add_all(exercises)

db.session.commit()
print("Database seeded with exercises!")
