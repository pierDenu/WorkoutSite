from flask import render_template

from app.models import Plan, Workout, PlanWorkout
from app.plans import plans_bp

# @plans_bp.route('/')
# def choose_plan():
#     plans = Plan.get_all()
#     return render_template("choose_plan.html", plans=plans)

@plans_bp.route('/create')
def create_plan():
    plan = Plan(name='New Plan')  # Temporary plan object, not saved to DB
    workouts = Workout.get_all()  # Assuming this retrieves all workouts from DB
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    schedule = {day: None for day in weekdays}  # Empty schedule to display placeholders
    return render_template("create_plan.html", plan=plan, schedule=schedule, workouts=workouts)

@plans_bp.route('/display/<string:plan_id>')
def display_plan(plan_id):
    plan = Plan.get_by_id(plan_id)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    schedule = {}
    for day in weekdays:
        workout_id = PlanWorkout.get_workout_id_by_plan_and_day(plan.id, day)
        schedule[day] = Workout.get_by_id(workout_id)
    return render_template("display_plan.html", plan=plan, schedule=schedule)
