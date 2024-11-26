<template>
  <div>
    <h1>Movies</h1>
    <ul>
      <li v-for="movie in movies" :key="movie.mid">
        <strong>{{ movie.title }}</strong>
        (Released: {{ movie.release_date }}, Rating: {{ movie.avg_rating }})
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      movies: []
    };
  },
  methods: {
    async fetchMovies() {
      try {
        const response = await fetch("http://127.0.0.1:5000/movies/search");
        const data = await response.json();
        this.movies = data;
      } catch (err) {
        console.error("Error fetching movies:", err);
      }
    }
  },
  mounted() {
    this.fetchMovies();
  }
};
</script>
