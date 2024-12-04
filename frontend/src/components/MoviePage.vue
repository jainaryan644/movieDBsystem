<template>
    <div class="movie-page">
      <MovieDetails :movie="movie" />
      <ReviewSection :reviews="reviews" @new-review="addReview" />
    </div>
  </template>
  
  <script>
  import MovieDetails from "./MovieDetails.vue";
  import ReviewSection from "./ReviewSection.vue";
  
  export default {
    data() {
      return {
        movie: {}, // Movie data to be passed as props
        reviews: [], // List of reviews
      };
    },
    components: {
      MovieDetails,
      ReviewSection,
    },
    methods: {
      addReview(newReview) {
        this.reviews.push(newReview);
      },
    },
  };
  </script>
  