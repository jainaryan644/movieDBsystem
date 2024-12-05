<template>
    <div class="movie-details">
        <h1>{{ movie.title }}</h1>
        <img :src="movie.poster" alt="Movie Poster" v-if="movie.poster" />
        <span class="simpleBox">
            <span v-for="n in 5" :key="n" :class="{'yellowStar':n <= avg_rating_rounded}">★</span>
            <span> {{ movie.avg_rating }}</span>
        </span>
        <p>{{ movie.description }}</p>
    </div>
</template>
  
<script>
    export default {
        props: ["movie"],
        return {
            avg_rating_rounded = Math.round(movie.avg_rating)
        };
    };
</script>

<style scoped>
    .simpleBox{
        outline: 3px solid black;
    }
    .yellowStar{
        color: gold;
    }
</style>