FROM postgres:16-alpine

# PostgreSQL executes these files alphabetically on first initialization.
COPY scripts/create_database.sql \
    /docker-entrypoint-initdb.d/00_create_database.sql

COPY schema/01_create_tables.sql \
    /docker-entrypoint-initdb.d/01_create_tables.sql

COPY schema/02_indexes.sql \
    /docker-entrypoint-initdb.d/02_indexes.sql

COPY schema/03_constraints.sql \
    /docker-entrypoint-initdb.d/03_constraints.sql

COPY seed/01_movies.sql \
    /docker-entrypoint-initdb.d/04_movies.sql