<template>
    <div v-if="movie" class="movie-details">
        <h1>{{ movie.title }}</h1>
        <img :src="movie.poster" alt="Movie Poster" v-if="movie.poster" />
        <span class="simpleBox">
            <span v-for="n in 5" :key="n" :class="{'yellowStar':n <= avg_rating_rounded}">★</span>
            &nbsp;<span> {{ movie.avg_rating }}</span> <!--&nbsp; adds the spacing between the stars and the numerical rating-->
        </span>
        <div class="simpleBox">
            <h3>Plot</h3>
            <p>{{ movie.plot }}</p>
        </div>
        
        <p>Released: {{ movie.release_date }}</p>
    </div>
</template>
  
<script>
    export default {
        props: ["movie"],
        data() {
            return {
                avg_rating_rounded: Math.round(this.movie.avg_rating),
            };
        },
        mounted() {

        },
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