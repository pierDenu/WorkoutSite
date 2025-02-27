from flask import render_template, request, jsonify

from app import db
from app.models import Plan, Workout, PlanWorkout
from app.plans import plans_bp
from app.plans.forms import PlanNameForm


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

@plans_bp.route('/create', methods=['GET'])
def create():
    plan = Plan(name='New Plan')  # Temporary plan object, not saved to DB
    workouts = Workout.get_all()  # Assuming this retrieves all workouts from DB
    return render_template("create_plan.html", plan=plan,
                           enable_drag_and_drop=True, days=days, workouts=workouts)


@plans_bp.route("/save", methods=["POST"])
def save_plan():
    try:
        data = request.get_json()
        plan_name = data.get("plan_name")

        if not plan_name:
            return jsonify({"error": "Plan name is required"}), 400

        # Створюємо новий план
        plan = Plan(name=plan_name)
        db.session.add(plan)
        db.session.flush()  # Отримуємо ID плану, але ще не коммітимо

        for day in days:
            workouts = data.get(day, {})  # Отримуємо тренування для конкретного дня

            for order, workout_id in workouts.items():
                plan_workout = PlanWorkout(
                    plan_id=plan.id,
                    workout_id=int(workout_id),  # Переконуємось, що ID є числом
                    day=day,
                    order=int(order)  # Переконуємось, що порядок є числом
                )
                db.session.add(plan_workout)

        db.session.commit()  # Зберігаємо зміни в базу
        return jsonify({"message": "Plan saved successfully!"}), 200

    except Exception as e:
        print(e)
        db.session.rollback()  # У разі помилки відкатуємо транзакцію
        return jsonify({"error": str(e)}), 500

@plans_bp.route("/search-workouts-by-name", methods=["GET"])
def search_by_name():
    workout_name = request.args.get("name", "").strip()
    if workout_name:
        workouts = Workout.search_by_name(workout_name)
    else:
        workouts = Workout.get_all()
    return render_template("workout_list.html", workouts=workouts)

@plans_bp.route("/", methods=["GET"])
def index():
    plan = Plan.query.first()  # Отримуємо план із БД
    if not plan:
        plan = Plan(name="New Plan")  # Якщо немає, створюємо тимчасовий

    plans = Plan.get_all()  # Завантажуємо всі плани
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return render_template("display_plan.html", days=days, plans=plans, plan=plan,
                           enable_drag_and_drop=False)

@plans_bp.route('/edit', methods=['GET'])
def edit():
    plan_id = request.args.get("plan_id")
    plan = Plan.query.get_or_404(plan_id)
    workouts = Workout.get_all()  # Assuming this retrieves all workouts from DB
    return render_template("create_plan.html", plan=plan,
                           enable_drag_and_drop=True, days=days, workouts=workouts)

