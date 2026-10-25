
-- WARNING: DESTRUCTIVE.
-- This permanently removes the application tables and their data.
-- Run only against a disposable development database.

BEGIN;

DROP TABLE IF EXISTS viewing_events CASCADE;
DROP TABLE IF EXISTS watchlist CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS movies CASCADE;

COMMIT;
