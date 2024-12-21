from flask import render_template, jsonify

from app.main import bp
from app.models import Plan, PlanWorkout
from app.models.associations import workout_exercise
from app.models.exercise import Exercise
from app.models.muscle_group import MuscleGroup
from app.models.workout import Workout
from app import db

@bp.route('/')
def index():
    return render_template("index.html")


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




@bp.route('/goida')
def goida():
    return render_template("goida.html")
