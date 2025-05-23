import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(port=5000, host="localhost", debug=debug_mode)
