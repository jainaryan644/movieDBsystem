<template>
    <div class="movie-details">
      <h1>{{ movie.title }}</h1>
      <img :src="movie.poster" alt="Movie Poster" v-if="movie.poster" />
      <p>{{ movie.description }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: ["movie"],
  };
  </script>
  