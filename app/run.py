from app import create_app, db

# Create the Flask application
app = create_app()
app.config["SECRET_KEY"] = "your_secret_key_here"

# Create database tables (if they don't exist yet)
with app.app_context():
    db.create_all()  # Create all tables defined in your models

@app.context_processor
def inject_defaults():
    return {'navbar_height': 50}

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
