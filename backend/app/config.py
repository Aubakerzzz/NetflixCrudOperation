
import os


class Config:
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "development-only-change-me",
    )

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///netflix_clone.db",
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FRONTEND_ORIGIN = os.getenv(
        "FRONTEND_ORIGIN",
        "http://localhost:5173",
    )
