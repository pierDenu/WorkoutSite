from flask import render_template, jsonify

from app.main import bp
from app.models.associations import workout_exercise
from app.models.exercise import Exercise
from app.models.muscle_group import MuscleGroup
from app.models.workout import Workout
from flask import request
from app import db

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/choose-workout')
def choose_workout():
    workouts = Workout.query.all()
    return render_template('choose_workout.html', workouts=workouts)

@bp.route('/create-workout')
def create_workout():
    # Retrieve all exercises from the database to display on the page
    exercises = Exercise.get_all()
    muscle_groups = MuscleGroup.get_all()

    return render_template('create_workout.html', all_exercises=exercises,
                           muscle_groups=muscle_groups)

@bp.route('/save-workout', methods=['POST'])
def save_workout():
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

@bp.route('/exercise-data-by-id/<int:id>')
def get_exercise_data(id):
    # Логіка для обробки запиту
    exercise = Exercise.query.get(id)
    if not exercise:
        return jsonify({"message": "Data not found"}), 404

    return jsonify(exercise.to_dict())

@bp.route('/search-exercise-name/', defaults={'exercise_name': ''})
@bp.route('/search-exercise-name/<string:exercise_name>')
def search_exercises_by_name(exercise_name):
    try:
        if exercise_name == '':
            exercises = Exercise.get_all()
        else:
            exercises = Exercise.search_by_name(exercise_name)

        if not exercises:
            return jsonify({"message": "Data not found"}), 404

        exercises = [exercise.to_dict() for exercise in exercises]

        return jsonify({'exercises': exercises})

    except Exception as e:
        # Log the error for debugging
        print(f"Error: {e}")
        return jsonify({"message": "An unexpected error occurred"}), 500

@bp.route('/search-exercise-muscle-group/<string:muscle_group_name>')
def search_exercises_by_muscle_group(muscle_group_name):
    try:
        muscle_group = MuscleGroup.query.filter_by(name=muscle_group_name).first()

        if not muscle_group:
            return jsonify({"message": "Data not found"}), 404

        exercises = muscle_group.exercises
        exercises = [exercise.to_dict() for exercise in exercises]
        return jsonify({'exercises': exercises})

    except Exception as e:
        # Log the error for debugging
        print(f"Error: {e}")
        return jsonify({"message": "An unexpected error occurred"}), 500