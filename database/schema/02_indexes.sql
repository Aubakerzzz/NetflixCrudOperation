
-- The primary key and users.email UNIQUE constraint already have indexes.

-- Supports common movie listing and filtering patterns.
CREATE INDEX IF NOT EXISTS idx_movies_title
    ON movies (title);

CREATE INDEX IF NOT EXISTS idx_movies_genre
    ON movies (genre);

CREATE INDEX IF NOT EXISTS idx_movies_year
    ON movies (year);

-- Supports fetching a user's watchlist by most recently added.
CREATE INDEX IF NOT EXISTS idx_watchlist_user_added
    ON watchlist (user_id, added_at DESC);

-- Supports analytics queries grouped by movie and event time.
CREATE INDEX IF NOT EXISTS idx_viewing_events_movie_time
    ON viewing_events (movie_id, occurred_at DESC);

-- Supports a user's viewing history.
CREATE INDEX IF NOT EXISTS idx_viewing_events_user_time
    ON viewing_events (user_id, occurred_at DESC);
