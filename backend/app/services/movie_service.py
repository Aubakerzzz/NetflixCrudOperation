from sqlalchemy import select

from app.extensions import db
from app.models.movie import Movie


def get_all_movies(search=None):
    statement = select(Movie).order_by(Movie.id.desc())

    if search:
        pattern = f"%{search.strip()}%"
        statement = statement.where(
            db.or_(
                Movie.title.ilike(pattern),
                Movie.genre.ilike(pattern),
            )
        )

    return db.session.execute(statement).scalars().all()


def get_movie_by_id(movie_id):
    return db.session.get(Movie, movie_id)


def create_movie(data):
    movie = Movie(
        title=data["title"].strip(),
        genre=data["genre"].strip(),
        year=data["year"],
        rating=data.get("rating", 7.0),
        poster=data.get("poster", "").strip(),
        description=data.get("description", "").strip(),
    )

    db.session.add(movie)
    db.session.commit()

    return movie


def update_movie(movie, data):
    for field in ("title", "genre", "year", "rating", "poster", "description"):
        if field in data:
            value = data[field]

            if field in ("title", "genre", "poster", "description"):
                value = value.strip()

            setattr(movie, field, value)

    db.session.commit()

    return movie


def delete_movie(movie):
    db.session.delete(movie)
    db.session.commit()