from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db
from app.services.movie_service import (
    create_movie,
    delete_movie,
    get_all_movies,
    get_movie_by_id,
    update_movie,
)

movie_bp = Blueprint("movies", __name__, url_prefix="/api/movies")

ALLOWED_FIELDS = {
    "title", "genre", "year", "rating", "poster", "description",
}
REQUIRED_FIELDS = {"title", "genre", "year"}


def validate_movie_data(data, partial=False):
    if not isinstance(data, dict):
        return "Request body must be a JSON object."

    unknown = set(data.keys()) - ALLOWED_FIELDS
    if unknown:
        return f"Unknown fields: {', '.join(sorted(unknown))}"

    if not partial:
        missing = REQUIRED_FIELDS - set(data.keys())
        if missing:
            return f"Missing required fields: {', '.join(sorted(missing))}"

    for field in ("title", "genre", "poster", "description"):
        if field in data:
            value = data[field]
            if not isinstance(value, str):
                return f"{field} must be a string."
            if field in ("title", "genre") and not value.strip():
                return f"{field} cannot be empty."

            max_lengths = {"title": 200, "genre": 100, "poster": 2048}
            if field in max_lengths and len(value) > max_lengths[field]:
                return f"{field} exceeds the maximum length."

    if "year" in data:
        year = data["year"]
        if isinstance(year, bool) or not isinstance(year, int):
            return "year must be an integer."
        if not 1888 <= year <= 2100:
            return "year must be between 1888 and 2100."

    if "rating" in data:
        rating = data["rating"]
        if (
            isinstance(rating, bool)
            or not isinstance(rating, (int, float))
            or not 0 <= rating <= 10
        ):
            return "rating must be a number between 0 and 10."

    return None


@movie_bp.get("")
def list_movies():
    search = request.args.get("search", "").strip()
    movies = get_all_movies(search or None)
    return jsonify([movie.to_dict() for movie in movies]), 200


@movie_bp.get("/<int:movie_id>")
def retrieve_movie(movie_id):
    movie = get_movie_by_id(movie_id)
    if movie is None:
        return jsonify({"error": "Movie not found."}), 404
    return jsonify(movie.to_dict()), 200


@movie_bp.post("")
def add_movie():
    data = request.get_json(silent=True)
    error = validate_movie_data(data)
    if error:
        return jsonify({"error": error}), 400

    try:
        movie = create_movie(data)
        return jsonify(movie.to_dict()), 201
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Could not create movie."}), 500


@movie_bp.route("/<int:movie_id>", methods=["PUT", "PATCH"])
def edit_movie(movie_id):
    data = request.get_json(silent=True)
    error = validate_movie_data(data, partial=request.method == "PATCH")
    if error:
        return jsonify({"error": error}), 400

    movie = get_movie_by_id(movie_id)
    if movie is None:
        return jsonify({"error": "Movie not found."}), 404

    try:
        movie = update_movie(movie, data)
        return jsonify(movie.to_dict()), 200
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Could not update movie."}), 500


@movie_bp.delete("/<int:movie_id>")
def remove_movie(movie_id):
    movie = get_movie_by_id(movie_id)
    if movie is None:
        return jsonify({"error": "Movie not found."}), 404

    try:
        delete_movie(movie)
        return jsonify({"message": "Movie deleted successfully."}), 200
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Could not delete movie."}), 500
