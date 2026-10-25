
# Database migrations

## Initial database setup

Apply the SQL files in this order:

1. ../schema/01_create_tables.sql
2. ../schema/02_indexes.sql
3. ../schema/03_constraints.sql
4. ../seed/01_movies.sql

## Future schema changes

- Never edit a migration that has already been applied to a shared database.
- Add a new numbered SQL migration for each schema change.
- Review and test the migration before applying it.
- Back up important data before production migrations.
- Record which migration versions have been applied.

Example future files:

- 004_add_movie_runtime.sql
- 005_add_genres.sql
- 006_add_recommendation_events.sql
