<template>
    <div v-if="movie">
      <h1>{{ movie.title }}</h1>
      <p>Released: {{ movie.release_date }}</p>
      <p>Rating: {{ movie.avg_rating }}</p>
      <ReviewSection :movieId="movie.mid" />
    </div>
    <div v-else>
      <p>Loading movie details...</p>
    </div>
  </template>
  
  <script>
  import ReviewSection from "./ReviewSection.vue";
  import axios from "axios";
  
  export default {
    components: {
      ReviewSection,
    },
    data() {
      return {
        movie: null, // Movie details
      };
    },
    mounted() {
      const movieId = this.$route.params.mid; // Get movie ID from route
      if (movieId) {
        this.fetchMovieDetails(movieId);
      }
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
  
  <style scoped>
  /* Add any specific styles here */
  </style>
  