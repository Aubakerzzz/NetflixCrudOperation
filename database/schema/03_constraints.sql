
-- Optional uniqueness rule for the current catalog.
-- Only enable if your product requirements prohibit duplicate titles
-- from the same release year.
--
-- CREATE UNIQUE INDEX IF NOT EXISTS uq_movies_title_year
--     ON movies (LOWER(title), year);

-- No additional constraints are required at this stage.
-- Core foreign keys, required fields, and range checks are in
-- 01_create_tables.sql.
