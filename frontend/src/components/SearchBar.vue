<template>
  <div class="search-bar">
    <input type="text" v-model="query" placeholder="Search for movie..." @input="searchMovies" />
    <ul v-if="results.length">
      <li v-for="movie in results" :key="movie.title"><router-link v-bind:to="'/movie/' + movie.mid">{{ movie.title }}</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: "",
      results: [],
    };
  },
  methods: {
    async searchMovies() {
      const response = await fetch("http://127.0.0.1:5000/movies/search/" + this.query);
      const data = await response.json();
      
      this.results = data.results;
    },
  },
};
</script>

<style scoped>
ul {
  background-color: white;
  margin-top: 0%;
  list-style-type: none; 
  padding: 0;
  width: 100px;
  justify-content: center;
}
</style>