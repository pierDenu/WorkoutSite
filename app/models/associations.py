from app import db

# Association table for many-to-many relationship between Workout and Exercise
workout_exercise = db.Table('workout_exercise',
    db.Column('workout_id', db.Integer, db.ForeignKey('workout.id'), primary_key=True),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'), primary_key=True),
    db.Column('reps', db.Integer, nullable=True),  # Number of reps for each exercise in the workout
    db.Column('rest_time', db.Integer, nullable=True),  # Rest time in seconds between sets
    db.Column('additional_weight', db.Integer, nullable=True),  # Additional weight (if needed)
    db.Column('order', db.Integer, nullable=False)  # Order of exercises within the workout
)
