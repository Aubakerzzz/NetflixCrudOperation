from app.extensions import db


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, index=True)
    genre = db.Column(db.String(100), nullable=False, index=True)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False, default=7.0)
    poster = db.Column(db.String(2048), nullable=False, default="")
    description = db.Column(db.Text, nullable=False, default="")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "year": self.year,
            "rating": self.rating,
            "poster": self.poster,
            "description": self.description,
        }