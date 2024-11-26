<template>
  <div>
    <h1>Test Movies</h1>
    <ul>
      <li v-for="movie in movies" :key="movie.mid">{{ movie.title }}</li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      movies: [], // Initialize empty array for movies
    };
  },
  mounted() {
    // Fetch movies from the Flask backend
    axios
      .get("http://127.0.0.1:5000/movies")
      .then((response) => {
        console.log("API Response:", response.data); // Log the response
        this.movies = response.data; // Set movies to the response data
      })
      .catch((error) => {
        console.error("Error fetching movies:", error);
      });
  },
};
</script>
