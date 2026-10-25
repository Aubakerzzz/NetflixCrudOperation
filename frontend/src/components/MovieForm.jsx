import { useEffect, useState } from "react";

const emptyMovie = {
  title: "",
  genre: "",
  year: new Date().getFullYear(),
  rating: 7,
  poster: "",
  description: "",
};

function MovieForm({ movieToEdit, onSave, onCancel }) {
  const [formData, setFormData] = useState(emptyMovie);

  useEffect(() => {
    setFormData(movieToEdit || emptyMovie);
  }, [movieToEdit]);

  function handleChange(event) {
    const { name, value } = event.target;

    setFormData((previous) => ({
      ...previous,
      [name]: value,
    }));
  }

  function handleSubmit(event) {
    event.preventDefault();

    onSave({
      ...formData,
      title: formData.title.trim(),
      genre: formData.genre.trim(),
      year: Number(formData.year),
      rating: Number(formData.rating),
      poster:
        formData.poster.trim() ||
        "https://placehold.co/300x420/181818/ffffff?text=Movie",
    });

    setFormData(emptyMovie);
  }

  return (
    <form className="movie-form" onSubmit={handleSubmit}>
      <h2>{movieToEdit ? "Update Movie" : "Add New Movie"}</h2>

      <label>
        Movie title
        <input
          name="title"
          value={formData.title}
          onChange={handleChange}
          placeholder="Enter movie title"
          required
        />
      </label>

      <label>
        Genre
        <input
          name="genre"
          value={formData.genre}
          onChange={handleChange}
          placeholder="e.g. Action, Drama, Sci-Fi"
          required
        />
      </label>

      <div className="form-row">
        <label>
          Release year
          <input
            type="number"
            name="year"
            min="1888"
            max="2100"
            value={formData.year}
            onChange={handleChange}
            required
          />
        </label>

        <label>
          Rating (0–10)
          <input
            type="number"
            name="rating"
            min="0"
            max="10"
            step="0.1"
            value={formData.rating}
            onChange={handleChange}
            required
          />
        </label>
      </div>

      <label>
        Poster image URL
        <input
          type="url"
          name="poster"
          value={formData.poster}
          onChange={handleChange}
          placeholder="https://example.com/poster.jpg"
        />
      </label>

      <label>
        Description
        <textarea
          name="description"
          value={formData.description}
          onChange={handleChange}
          placeholder="Write a short description"
          rows="3"
        />
      </label>

      <div className="form-actions">
        <button type="submit" className="primary-button">
          {movieToEdit ? "Save Changes" : "Create Movie"}
        </button>

        {movieToEdit && (
          <button
            type="button"
            className="secondary-button"
            onClick={onCancel}
          >
            Cancel
          </button>
        )}
      </div>
    </form>
  );
}

export default MovieForm;