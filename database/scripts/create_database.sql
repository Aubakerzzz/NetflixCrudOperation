
-- Create the project database.
-- Run this while connected to the default "postgres" database.

SELECT 'CREATE DATABASE netflix_clone'
WHERE NOT EXISTS (
    SELECT FROM pg_database
    WHERE datname = 'netflix_clone'
)\gexec
