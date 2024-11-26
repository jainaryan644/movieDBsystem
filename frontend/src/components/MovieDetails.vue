<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <p>{{ movie.plot }}</p>
    <p>Release Date: {{ movie.release_date }}</p>
    <p>Genres: {{ movie.genres.join(", ") }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      movie: null,
    };
  },
  async created() {
    const movieId = this.$route.params.id;
    await this.fetchMovieDetails(movieId);
  },
  methods: {
    async fetchMovieDetails(movieId) {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/movies/${movieId}`);
        this.movie = response.data;
      } catch (error) {
        console.error("Error fetching movie details:", error);
      }
    },
  },
};
</script>
