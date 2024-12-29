from app import db
from app.models import workout_exercise
from app.run import app
from app.models.workout import Workout
from app.models.exercise import Exercise

# List of exercises
exercises = [
    'Push-Ups', 'Dips', 'Weighted Dips', 'Pull-Ups',
    'Weighted Pull-Ups', 'Pike Push-Ups', 'Handstand Push-Ups'
]

# Use the application context
with app.app_context():
    # Creating a dozen workouts
    workouts = []
    for i in range(1, 13):  # Loop for 12 workouts
        workout_name = f"Workout {i}"
        workout_duration = 30 + i * 5  # Assign a duration incrementally (e.g., 35, 40, etc.)
        workout = Workout(name=workout_name, duration=workout_duration)
        exercise_name = exercises[i%len(exercises)]
        exercise = Exercise.get_by_name(exercise_name)
        weight = i*5 if(exercise.needs_additional_weight) else None

        workout_exercise_entry = workout_exercise.insert().values(
            workout_id=workout.id,
            exercise_id=exercise.id,
            reps=i,
            rest_time=i*10,
            additional_weight=weight,
            order=1  # Ensure the order is saved
        )

        workouts.append(workout)
        db.session.add(workout)

    # Commit the workouts to the database
    db.session.commit()

print("12 workouts created successfully!")
