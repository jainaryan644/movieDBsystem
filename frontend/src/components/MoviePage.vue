<template>
    <div class="movie-page">
        <NavBar />
        <MovieDetails :movie="movie" />
        <ReviewSection :reviews="reviews" @new-review="addReview" />
    </div>
</template>
  
<script>
    import MovieDetails from "./MovieDetails.vue";
    import ReviewSection from "./ReviewSection.vue";
    import NavBar from "./NavBar.vue";
  
    export default {
        data() {
            return {
                movie: {}, // Movie data to be passed as props
                reviews: [], // List of reviews
                error: "",
            };
        },
        components: {
            MovieDetails,
            ReviewSection,
        },
        methods: {
            async getMovieAndReviews() {
                const movieResponse = await fetch(`http://127.0.0.1:5000/movies/${$route.params.mid}`);
                const movieData = await movieResponse.json();
                if json.stringify(movieData) === "{}"{$router.push("/");}
                this.movie = movieData;
                const reviewsResponse = await fetch(`http://127.0.0.1:5000/reviews/movie/${$route.params.mid}`);
                const reviewsData = await reviewsResponse.json();
                this.reviews = reviewsData.results;
            }
            async addReview(newReview) {
                const pushReviewResponse = await fetch(`http://127.0.0.1:5000/reviews/add`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        uid: localStorage.getItem("userId"),
                        mid: this.movie.mid,
                        comment: newReview.comment,
                        rating: newReview.rating,
                    }),
                });
                if (!pushReviewResponse.ok) {
                    const errorData = await pushReviewResponse.json();
                    this.error = errorData.message || "Login failed. Please try again.";
                    return;
                }
                const pushReviewData = await pushReviewResponse.json();
                getMovieAndReviews();
            },
        },
        mounted() {
            this.getMovieAndReviews(); // Populate the movie data and list of reviews
        },
    };
</script>
  