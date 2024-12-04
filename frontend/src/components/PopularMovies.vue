<template>
  <div class="popular-movies">
    <h2>Popular Movies</h2>
    <ul>
      <li v-for="movie in topMovies" :key="movie.id">{{ movie.title }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      topMovies: [], // Populate this with API data
    };
  },
  mounted() {
    // Fetch top 5 movies here
  },
};
</script>
