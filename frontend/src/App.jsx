
import { useCallback, useEffect, useMemo, useState } from "react";
import MovieForm from "./components/MovieForm";
import MovieList from "./components/MovieList";

import {
  getMovies,
  createMovie,
  updateMovie,
  deleteMovie,
} from "./services/movieService";

function App() {
  const [movies, setMovies] = useState([]);
  const [movieToEdit, setMovieToEdit] = useState(null);
  const [search, setSearch] = useState("");
  const [showForm, setShowForm] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadMovies = useCallback(async () => {
    try {
      setError("");
      const data = await getMovies();
      setMovies(data);
    } catch (err) {
      setError(err.message || "Failed to load movies.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadMovies();
  }, [loadMovies]);

  const filteredMovies = useMemo(() => {
    const query = search.toLowerCase().trim();

    return movies.filter(
      (movie) =>
        movie.title.toLowerCase().includes(query) ||
        movie.genre.toLowerCase().includes(query)
    );
  }, [movies, search]);

  async function handleSave(movieData) {
    try {
      setError("");

      if (movieToEdit) {
        await updateMovie(movieToEdit.id, movieData);
      } else {
        await createMovie(movieData);
      }

      await loadMovies();
      setMovieToEdit(null);
      setShowForm(false);
    } catch (err) {
      setError(err.message || "Failed to save movie.");
    }
  }

  function handleEdit(movie) {
    setMovieToEdit(movie);
    setShowForm(true);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  async function handleDelete(id) {
    const confirmed = window.confirm(
      "Are you sure you want to delete this movie?"
    );

    if (!confirmed) return;

    try {
      setError("");
      await deleteMovie(id);

      if (movieToEdit?.id === id) {
        setMovieToEdit(null);
        setShowForm(false);
      }

      await loadMovies();
    } catch (err) {
      setError(err.message || "Failed to delete movie.");
    }
  }

  function handleCancel() {
    setMovieToEdit(null);
    setShowForm(false);
  }

  return (
    <div className="app">
      <header className="navbar">
        <a className="brand" href="/">
          NETFLIX
        </a>

        <span className="admin-label">Movie Management</span>
      </header>

      <main className="container">
        <section className="hero">
          <p className="eyebrow">NETFLIX CLONE · ADMIN</p>
          <h1>Manage your movie library.</h1>
          <p className="hero-description">
            Create, view, update, and delete movies from your collection.
          </p>

          <div className="toolbar">
            <input
              className="search-input"
              type="search"
              placeholder="Search by movie title or genre..."
              value={search}
              onChange={(event) => setSearch(event.target.value)}
            />

            <button
              type="button"
              className="primary-button add-button"
              onClick={() => {
                setMovieToEdit(null);
                setShowForm((previous) => !previous);
              }}
            >
              {showForm && !movieToEdit ? "Close Form" : "+ Add Movie"}
            </button>
          </div>
        </section>

        {error && (
          <p role="alert" className="error-message">
            {error}
          </p>
        )}

        {showForm && (
          <section className="form-section">
            <MovieForm
              movieToEdit={movieToEdit}
              onSave={handleSave}
              onCancel={handleCancel}
            />
          </section>
        )}

        <section className="library-section">
          <div className="section-heading">
            <h2>Movie Library</h2>
            <span>{filteredMovies.length} movies</span>
          </div>

          {loading ? (
            <p>Loading movies...</p>
          ) : (
            <MovieList
              movies={filteredMovies}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          )}
        </section>
      </main>

      <footer className="footer">
        Netflix Clone · Frontend Activity 2
      </footer>
    </div>
  );
}

export default App;
