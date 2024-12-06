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
  methods: {
    async fetchTopMovies(){
      const response = await fetch("http://127.0.0.1:5000/movies/top");
      const data = await response.json();

      this.topMovies = data.results;
    }
  },

  mounted() {
    // Fetch top 5 movies here
    fetchTopMovies();
  },
};
</script>
