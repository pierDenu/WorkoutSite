from flask import render_template, jsonify, request

from app.models import Workout, Exercise, MuscleGroup, workout_exercise
from app.workouts import workouts_bp
from app import db


@workouts_bp.route('/')
def choose():
    workouts = Workout.query.all()
    return render_template('choose_workout.html', workouts=workouts)


@workouts_bp.route('/create')
def create():
    exercises = Exercise.get_all()
    muscle_groups = MuscleGroup.get_all()
    return render_template('create_workout.html', all_exercises=exercises,
                           muscle_groups=muscle_groups)


@workouts_bp.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    workout_data = data.get('workout')

    try:
        workout = Workout(name=workout_data['name'], duration=workout_data['duration'])
        db.session.add(workout)
        db.session.flush()

        for exercise_data in workout_data['exercises']:
            exercise = db.session.get(Exercise, exercise_data['exercise_id'])
            db.session.execute(workout_exercise.insert().values(
                workout_id=workout.id,
                exercise_id=exercise.id,
                reps=exercise_data['reps'],
                rest_time=exercise_data['rest_time'],
                additional_weight=exercise_data['additional_weight'],
                order=exercise_data['order'],
            ))

        db.session.commit()
        return jsonify({'message': 'Workout saved successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error saving workout', 'error': str(e)}), 500
