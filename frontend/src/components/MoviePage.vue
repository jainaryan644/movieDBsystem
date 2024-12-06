<template>
    <NavBar @new-page="newPageSelected"/>
    <div :key="reload_var">
    <MovieDetails  v-if="movie" :movie="movie"/>
    <!-- <div v-if="movie"> 
      <h1>{{ movie.title }}</h1>
      <p>Released: {{ movie.release_date }}</p>
      <p>Rating: {{ movie.avg_rating }}</p>
      <ReviewSection :movieId="movie.mid" />
    </div> -->
    <div v-else>
      <p>Loading movie details...</p>
    </div>
    <ReviewSection v-if="movie" :movieId="movie.mid"/>
    </div>
  </template>
  
  <script>
  import ReviewSection from "./ReviewSection.vue";
  import MovieDetails from "./MovieDetails.vue";
  import NavBar from "./NavBar.vue";
  import axios from "axios";
  
  export default {
    watch: {
        'this.$route.params.id': function () {
            this.$route.push(0);
        },
    },
    components: {
      ReviewSection,
      MovieDetails,
      NavBar,
    },
    data() {
      return {
        movie: null, // Movie details
        reload_var: 0,
      };
    },
    mounted() {
      //const movieId = this.$route.params.mid; // Get movie ID from route
      this.fetchMovieDetails(this.$route.params.mid);
      // if (movieId) {
      //   this.fetchMovieDetails(movieId);
      // }
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
      newPageSelected(){
        this.fetchMovieDetails(this.$route.params.mid);
        
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add any specific styles here */
  </style>
  