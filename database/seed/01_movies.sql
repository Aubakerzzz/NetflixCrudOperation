
INSERT INTO movies (id, title, genre, year, rating, poster, description)
VALUES
(
    1,
    'Stranger Things',
    'Sci-Fi',
    2022,
    8.7,
    'https://placehold.co/300x420/181818/ffffff?text=Stranger+Things',
    'A group of friends uncover mysterious supernatural events.'
),
(
    2,
    'The Dark Knight',
    'Action',
    2008,
    9.0,
    'https://placehold.co/300x420/181818/ffffff?text=The+Dark+Knight',
    'Batman faces a dangerous criminal known as the Joker.'
),
(
    3,
    'Inception',
    'Sci-Fi',
    2010,
    8.8,
    'https://placehold.co/300x420/181818/ffffff?text=Inception',
    'A skilled thief enters peoples dreams to steal secrets.'
),
(
    4,
    'Interstellar',
    'Sci-Fi',
    2014,
    8.7,
    'https://placehold.co/300x420/181818/ffffff?text=Interstellar',
    'Explorers search for a future for humanity beyond Earth.'
),
(
    5,
    'The Shawshank Redemption',
    'Drama',
    1994,
    9.3,
    'https://placehold.co/300x420/181818/ffffff?text=Shawshank',
    'Two prisoners develop a friendship over many years.'
)
ON CONFLICT (id) DO NOTHING;

-- Keep the generated ID sequence aligned with explicit seed IDs.
SELECT setval(
    pg_get_serial_sequence('movies', 'id'),
    COALESCE((SELECT MAX(id) FROM movies), 1),
    EXISTS (SELECT 1 FROM movies)
);
