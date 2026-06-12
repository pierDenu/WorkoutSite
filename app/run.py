import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

app = create_app()

@app.context_processor
def inject_defaults():
    return {'navbar_height': 50}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
