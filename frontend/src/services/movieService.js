
const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:5000";

  
const MOVIES_URL = `${API_BASE_URL}/api/movies`;

async function request(url, options = {}) {
  const response = await fetch(url, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
  });

  const data = await response.json().catch(() => null);

  if (!response.ok) {
    throw new Error(
      data?.error || `API request failed with status ${response.status}`
    );
  }

  return data;
}

export async function getMovies(search = "") {
  const url = new URL(MOVIES_URL);

  if (search.trim()) {
    url.searchParams.set("search", search.trim());
  }

  return request(url.toString());
}

export async function getMovieById(id) {
  return request(`${MOVIES_URL}/${id}`);
}

export async function createMovie(movie) {
  return request(MOVIES_URL, {
    method: "POST",
    body: JSON.stringify(movie),
  });
}

export async function updateMovie(id, movie) {
  return request(`${MOVIES_URL}/${id}`, {
    method: "PUT",
    body: JSON.stringify(movie),
  });
}

export async function deleteMovie(id) {
  return request(`${MOVIES_URL}/${id}`, {
    method: "DELETE",
  });
}
