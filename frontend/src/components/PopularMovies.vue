<template>
  <div class="popular-movies" id="popMovies">
    <h2>Popular Movies</h2>
    <hr style="width: 50%;">
    <ol class="movie-list">
      <li v-for="(movie, index) in topMovies" :key="movie.mid" class="movie-item">
        <div class="movie-entry">
          <span class="movie-rank">{{ index + 1 }}.</span>
          <router-link :to="'/movie/' + movie.mid" class="movie-title">
            {{ movie.title }}
          </router-link>
          <span class="average-rating">⭐ {{ movie.avg_rating.toFixed(1) }}</span>
        </div>
      </li>
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
    async fetchTopMovies() {
      try {
        const response = await fetch("http://127.0.0.1:5000/movies/top");
        if (response.ok) {
          const data = await response.json();
          this.topMovies = data; // Update the topMovies list with fetched data
        } else {
          console.error("Failed to fetch top movies.");
        }
      } catch (error) {
        console.error("Error fetching top movies:", error);
      }
    },
  },

  mounted() {
    // Fetch top 5 movies when the component mounts
    this.fetchTopMovies();
  },
};
</script>


<style scoped>
#popMovies {
  text-align: center;
  margin-top: 2rem;
}

.popular-movies h2 {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.movie-list {
  list-style: none;
  padding: 0;
  margin: 0 auto;
  width: 50%; /* Center the list within the container */
}

.movie-item {
  margin: 0.5rem 0;
  font-size: 1.2rem;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.movie-entry {
  display: grid;
  grid-template-columns: 2rem 1fr auto; /* Adjust columns for number, title, and rating */
  gap: 1rem;
  width: 100%;
}

.movie-rank {
  text-align: right;
  font-weight: bold;
}

.movie-title {
  text-decoration: none;
  color: #007bff;
  font-weight: bold;
  text-align: left;
}

.movie-title:hover {
  color: #0056b3;
  text-decoration: underline;
}

.average-rating {
  font-size: 1rem;
  font-weight: bold;
  color: gold;
  text-align: right;
}
</style>
