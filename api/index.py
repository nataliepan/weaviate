"""App entry point."""
"""Initialize Flask app."""
import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_mail import Mail
from server import db, mail
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    CORS(app)

 

    @app.route("/api/json")
    def hello_json():
        return jsonify({"message": f"Hello, World! {OPENAI_API_KEY}."})

    # app.config.from_object("config.Config")

    # api = Api(app=app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
