import pytest

from app import create_app
from app.extensions import db


@pytest.fixture()
def client():
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite://",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "AUTO_CREATE_TABLES": True,
        }
    )

    with app.test_client() as test_client:
        with app.app_context():
            db.drop_all()
            db.create_all()

        yield test_client

        with app.app_context():
            db.session.remove()
            db.drop_all()


def sample_movie():
    return {
        "title": "Inception",
        "genre": "Sci-Fi",
        "year": 2010,
        "rating": 8.8,
        "poster": "https://example.com/inception.jpg",
        "description": "A dream-based science fiction thriller.",
    }


def test_health_check(client):
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_create_and_read_movie(client):
    response = client.post("/api/movies", json=sample_movie())

    assert response.status_code == 201
    movie_id = response.json["id"]
    assert response.json["title"] == "Inception"

    read_response = client.get(f"/api/movies/{movie_id}")

    assert read_response.status_code == 200
    assert read_response.json["genre"] == "Sci-Fi"


def test_list_movies(client):
    client.post("/api/movies", json=sample_movie())

    response = client.get("/api/movies")

    assert response.status_code == 200
    assert len(response.json) == 1


def test_search_movies(client):
    client.post("/api/movies", json=sample_movie())

    response = client.get("/api/movies?search=inception")

    assert response.status_code == 200
    assert len(response.json) == 1


def test_update_movie(client):
    created = client.post("/api/movies", json=sample_movie())
    movie_id = created.json["id"]

    response = client.patch(
        f"/api/movies/{movie_id}",
        json={"title": "Inception Updated"},
    )

    assert response.status_code == 200
    assert response.json["title"] == "Inception Updated"


def test_delete_movie(client):
    created = client.post("/api/movies", json=sample_movie())
    movie_id = created.json["id"]

    response = client.delete(f"/api/movies/{movie_id}")

    assert response.status_code == 200
    assert client.get(f"/api/movies/{movie_id}").status_code == 404


def test_reject_invalid_rating(client):
    movie = sample_movie()
    movie["rating"] = 15

    response = client.post("/api/movies", json=movie)

    assert response.status_code == 400


def test_reject_missing_required_fields(client):
    response = client.post(
        "/api/movies",
        json={"title": "Incomplete Movie"},
    )

    assert response.status_code == 400