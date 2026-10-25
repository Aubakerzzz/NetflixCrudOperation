function MovieCard({ movie, onEdit, onDelete }) {
  return (
    <article className="movie-card">
      <img
        className="movie-poster"
        src={movie.poster}
        alt={`${movie.title} poster`}
        onError={(event) => {
          event.currentTarget.src =
            "https://placehold.co/300x420/181818/ffffff?text=No+Poster";
        }}
      />

      <div className="movie-info">
        <h3>{movie.title}</h3>

        <div className="movie-meta">
          <span>{movie.year}</span>
          <span>{movie.genre}</span>
          <span className="rating">★ {movie.rating}/10</span>
        </div>

        <p>{movie.description || "No description available."}</p>

        <div className="card-actions">
          <button
            type="button"
            className="edit-button"
            onClick={() => onEdit(movie)}
          >
            Edit
          </button>

          <button
            type="button"
            className="delete-button"
            onClick={() => onDelete(movie.id)}
          >
            Delete
          </button>
        </div>
      </div>
    </article>
  );
}

export default MovieCard;