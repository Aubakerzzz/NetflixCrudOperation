
# Netflix Clone Database

Database engine: PostgreSQL

## Tables

- movies: movie catalog and metadata
- users: user profiles and password hashes
- watchlist: movies saved by users
- viewing_events: playback events for analytics

## Prerequisites

- PostgreSQL installed and running
- A database named netflix_clone
- A PostgreSQL account with permission to create tables and indexes

## Initial setup

Create the database if it does not exist:

    createdb -U postgres netflix_clone

Run the SQL files from the repository root:

    psql -U postgres -d netflix_clone -v ON_ERROR_STOP=1 -f database/schema/01_create_tables.sql

    psql -U postgres -d netflix_clone -v ON_ERROR_STOP=1 -f database/schema/02_indexes.sql

    psql -U postgres -d netflix_clone -v ON_ERROR_STOP=1 -f database/schema/03_constraints.sql

    psql -U postgres -d netflix_clone -v ON_ERROR_STOP=1 -f database/seed/01_movies.sql

## Verify

Connect to the database:

    psql -U postgres -d netflix_clone

List tables:

    \dt

Read sample movies:

    SELECT id, title, genre, year, rating FROM movies ORDER BY id;

Check the table structure:

    \d movies

## Docker

When PostgreSQL runs in Docker, mount the ordered schema and seed SQL files into the container's /docker-entrypoint-initdb.d/ directory.

The official PostgreSQL image runs initialization scripts only when initializing a new, empty data directory. Existing persistent volumes are not automatically reseeded.

Never store database passwords in this README or commit .env files.
