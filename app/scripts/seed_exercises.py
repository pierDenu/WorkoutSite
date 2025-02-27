from app import db
from app.run import app
from app.models.exercise import Exercise
from app.models.muscle_group import MuscleGroup

# Database reset function
def reset_database():
    db.drop_all()
    db.create_all()
    print("Database has been reset.")

# Seed data function
def seed_data():
    # Unique muscle groups
    muscle_groups_data = [
        "Abs",
        "Back",
        "Biceps",
        "Chest",
        "Legs",
        "Triceps",
        "Shoulders"
    ]

    # Create muscle groups
    muscle_group_objects = {}
    for group_name in muscle_groups_data:
        group = MuscleGroup.query.filter_by(name=group_name).first()
        if not group:
            group = MuscleGroup(name=group_name)
            db.session.add(group)
        muscle_group_objects[group_name] = group

    db.session.commit()

    # Exercises with associated muscle groups
    exercises_data = [
        {"name": "Push-Ups", "difficulty": "Medium", "muscle_groups": ["Chest", "Triceps"], "needs_additional_weight": False},
        {"name": "Dips", "difficulty": "Medium", "muscle_groups": ["Chest", "Triceps"], "needs_additional_weight": False},
        {"name": "Weighted Dips", "difficulty": "Hard", "muscle_groups": ["Chest", "Triceps"], "needs_additional_weight": True},
        {"name": "Pull-Ups", "difficulty": "Medium", "muscle_groups": ["Back", "Biceps"], "needs_additional_weight": False},
        {"name": "Weighted Pull-Ups", "difficulty": "Hard", "muscle_groups": ["Back", "Biceps"], "needs_additional_weight": True},
        {"name": "Pike Push-Ups", "difficulty": "Medium", "muscle_groups": ["Shoulders"], "needs_additional_weight": False},
        {"name": "Handstand Push-Ups", "difficulty": "Hard", "muscle_groups": ["Shoulders"], "needs_additional_weight": False},
    ]

    # Add exercises
    for exercise_data in exercises_data:
        exercise = Exercise.query.filter_by(name=exercise_data["name"]).first()
        if not exercise:
            exercise = Exercise(
                name=exercise_data["name"],
                difficulty=exercise_data["difficulty"],
                needs_additional_weight=exercise_data["needs_additional_weight"]
            )

            for group_name in exercise_data["muscle_groups"]:
                if group_name in muscle_group_objects:
                    exercise.muscle_groups.append(muscle_group_objects[group_name])

            db.session.add(exercise)

    db.session.commit()
    print("Database seeded with exercises and muscle groups!")

# Main execution
if __name__ == "__main__":
    with app.app_context():
        seed_data()
