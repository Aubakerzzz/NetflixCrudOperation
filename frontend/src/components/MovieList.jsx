import MovieCard from "./MovieCard";

function MovieList({ movies, onEdit, onDelete }) {
  if (movies.length === 0) {
    return (
      <div className="empty-state">
        <h2>No movies found</h2>
        <p>Add a movie or change your search.</p>
      </div>
    );
  }

  return (
    <div className="movie-grid">
      {movies.map((movie) => (
        <MovieCard
          key={movie.id}
          movie={movie}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}

export default MovieList;