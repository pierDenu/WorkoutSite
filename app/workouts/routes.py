from flask import render_template, jsonify
from flask import request

from app.models import Workout, Exercise, MuscleGroup, workout_exercise
from app.workouts import workouts_bp

from app import db

@workouts_bp.route('/')
def choose():
    workouts = Workout.query.all()
    return render_template('choose_workout.html', workouts=workouts)

@workouts_bp.route('/create')
def create():
    # Retrieve all exercises from the database to display on the page
    exercises = Exercise.get_all()
    muscle_groups = MuscleGroup.get_all()

    return render_template('create_workout.html', all_exercises=exercises,
                           muscle_groups=muscle_groups)

@workouts_bp.route('/save', methods=['POST'])
def save():
    data = request.get_json()  # Parse the JSON body of the request
    workout_data = data.get('workout')

    try:
        # Create a new workout record
        workout = Workout(name=workout_data['name'], duration=workout_data['duration'])
        db.session.add(workout)
        db.session.commit()  # Commit to get the workout ID

        # Add exercises to the workout using the association table
        for exercise_data in workout_data['exercises']:
            exercise = Exercise.query.get(exercise_data['exercise_id'])  # Get the exercise from the DB

            # Create a new association between the workout and the exercise
            workout_exercise_entry = workout_exercise.insert().values(
                workout_id=workout.id,
                exercise_id=exercise.id,
                reps=exercise_data['reps'],
                rest_time=exercise_data['rest_time'],
                additional_weight=exercise_data['additional_weight'],
                order=exercise_data['order']  # Ensure the order is saved
            )
            db.session.execute(workout_exercise_entry)

        db.session.commit()  # Commit all changes

        return jsonify({'message': 'Workout saved successfully!'}), 200
    except Exception as e:
        db.session.rollback()  # Rollback on error
        return jsonify({'message': 'Error saving workout', 'error': str(e)}), 500
