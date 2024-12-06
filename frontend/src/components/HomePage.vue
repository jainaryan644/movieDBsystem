<template>
  <div class="home-page">
    <NavBar />
    <PopularMovies />
  </div>
</template>

<script>
import NavBar from "./NavBar.vue";
// import SearchBar from "./SearchBar.vue";
import PopularMovies from "./PopularMovies.vue";


export default {
  components: {
    NavBar,
    PopularMovies,
  },
};
</script>
