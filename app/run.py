from app import create_app, db

# Create the Flask application
app = create_app()

# Create database tables (if they don't exist yet)
with app.app_context():
    db.create_all()  # Create all tables defined in your models

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
