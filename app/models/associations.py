from app import db  # Import the db instance from the main app

# Association table for the many-to-many relationship
workout_exercises = db.Table('workout_exercises',
    db.Column('workout_id', db.Integer, db.ForeignKey('workout.id'), primary_key=True),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'), primary_key=True)
)
