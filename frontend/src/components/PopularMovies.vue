<template>
  <div class="popular-movies" id="popMovies">
    <h2>Popular Movies</h2>
    <hr style="width: 50%;">
    <ol style="list-style-position: inside;">
      <li v-for="movie in topMovies" :key="movie.mid"><router-link :to="'/movie/' + movie.mid">{{ movie.title }}</router-link> {{ movie.avg_rating }}</li>
    </ol>
  </div>
</template>

<script>
export default {
  data() {
    return {
      topMovies: [],
    };
  },
  methods: {
    async fetchTopMovies(){
      const response = await fetch("http://127.0.0.1:5000/movies/top");
      const data = await response.json();
      
      this.topMovies = data;
    }
  },

  mounted() {
    // Fetch top 5 movies here
    this.fetchTopMovies();
  },
};
</script>
<style>
  #popMovies {
    text-align: center;
  }
</style>