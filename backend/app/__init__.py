
import os

from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy.exc import SQLAlchemyError

from app.config import Config
from app.extensions import db
from app.models import Movie
from app.routes import movie_bp


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)

    allowed_origin = os.getenv(
        "FRONTEND_ORIGIN",
        "http://localhost:5173",
    )

    CORS(
        app,
        resources={
            r"/api/*": {
                "origins": [allowed_origin]
            }
        },
    )

    db.init_app(app)

    # movie_bp already has the /api/movies URL prefix.
    app.register_blueprint(movie_bp)

    @app.get("/api/health")
    def health_check():
        return jsonify({"status": "ok"}), 200

    @app.errorhandler(404)
    def not_found(_error):
        return jsonify({"error": "Resource not found."}), 404

    @app.errorhandler(500)
    def internal_error(_error):
        db.session.rollback()
        return jsonify({"error": "Internal server error."}), 500

    # For local development only.
    # Use database migrations in production.
    if app.config.get("AUTO_CREATE_TABLES", False):
        with app.app_context():
            db.create_all()

    return app
