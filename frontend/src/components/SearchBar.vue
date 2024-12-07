<template>
  <div class="search-bar">
    <input
      type="text"
      v-model="query"
      placeholder="Search for movie..."
      @input="searchMovies"
      class="search-input"
    />
    <ul v-if="results.length" class="search-results">
      <li v-for="movie in results" :key="movie.mid">
        <router-link
          :to="'/movie/' + movie.mid"
          @click="clearSearch"
          class="search-result-item"
        >
          {{ movie.title }}
        </router-link>
      </li>
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
      if (this.query.trim() === "") {
        this.results = [];
        return;
      }
      try {
        const response = await fetch(
          "http://127.0.0.1:5000/movies/search/" + encodeURIComponent(this.query)
        );
        if (response.ok) {
          const data = await response.json();
          this.results = data.results || [];
        } else {
          console.error("Error fetching search results");
          this.results = [];
        }
      } catch (error) {
        console.error("Search error:", error);
        this.results = [];
      }
    },
    clearSearch() {
      this.query = "";
      this.results = [];
    },
  },
};
</script>

<style scoped>
.search-bar {
  position: relative;
  width: 600px;
}

.search-input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  outline: none;
  font-size: 1rem;
}

.search-results {
  position: absolute;
  top: 100%;
  left: 0;
  width: 102.5%; /* Tweaked value to align with search bar, dunno why it's finnicky */
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 5px;
  max-height: 200px;
  overflow-y: auto;
  z-index: 1000;
  list-style: none;
  padding: 0;
  margin: 0;
}
a {
  color: black;
}

.search-result-item {
  display: block;
  padding: 0.5rem;
  text-decoration: none;
  color: black;
  cursor: pointer;
}

.search-result-item:hover {
  background-color: #f0f0f0;
}
</style>
