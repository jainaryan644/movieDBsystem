<template>
  <NavBar />
  <MovieDetails v-if="movie" :movie="movie"/>
  <div v-else>
    <p>Loading movie details...</p>
  </div>
  <ReviewSection v-if="movie" :movieId="movie.mid"/>
</template>

<script>
import ReviewSection from "./ReviewSection.vue";
import MovieDetails from "./MovieDetails.vue";
import NavBar from "./NavBar.vue";
import axios from "axios";

export default {
  components: {
    ReviewSection,
    MovieDetails,
    NavBar,
  },
  data() {
    return {
      movie: null, // Movie details
    };
  },
  async mounted() {
    await this.fetchMovieDetails(this.$route.params.mid);
  },
  watch: {
    $route(to, from) {
      // Only fetch movie details if the `mid` has changed
      if (to.params.mid !== from.params.mid) {
        this.fetchMovieDetails(to.params.mid);
      }
    },
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
