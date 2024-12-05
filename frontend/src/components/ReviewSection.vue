<template>
    <div class="review-section">
        <form v-if="isLoggedIn" @submit.prevent="submitReview">
            <textarea v-model="newReview.text" placeholder="Leave a review..."></textarea>
            <select v-model="newReview.rating">
                <option v-for="star in 5" :value="star">{{ star }} Stars</option>
            </select>
            <button type="submit">Submit</button>
        </form>
        <p v-else>Please <router-link to="/login">Log In</router-link> To Leave a Review</p>
        <ul style="list-style-type: none;">
            <li v-for="review in reviews" :key="review.id">
                <div>
                    <span><b>{{ review.name }}</b></span>
                    <br>
                    <span class="simpleBox">
                        <span v-for="n in 5" :key="n" :class="{'yellowStar':n <= review.rating}">★</span>
                    </span>
                </div>
                <blockquote>{{ review.text }}</blockquote>
            </li>
        </ul>
    </div>
</template>
  
  <script>
  export default {
    props: ["reviews"],
    data() {
      return {
        isLoggedIn: !!localStorage.getItem("userId"), // Check login status from localStorage
        username: "", // Store the username
        newReview: {
            comment: "",
            rating: 0,
        },
        reviews: [],
      };
    },
    methods: {

        async fetchUsername() {
            try {
                const userId = localStorage.getItem("userId");
                if (userId) {
                    // Fetch username from the backend
                    const response = await fetch(`http://127.0.0.1:5000/users/${userId}`);
                    if (response.ok) {
                        const data = await response.json();
                        this.username = data.username;
                        this.isLoggedIn = true;
                    } else {
                        // If the response isn't OK, clear login status
                        this.isLoggedIn = false;
                        this.username = "";
                    }
                } else {
                    // If there's no userId in localStorage
                    this.isLoggedIn = false;
                    this.username = "";
                }
            } catch (error) {
                console.error("Failed to fetch username:", error);
                this.isLoggedIn = false;
            }
        },
        submitReview() {
            if this.newReview.rating < 1 {return;}
            this.$emit("new-review", { ...this.newReview });
            this.newReview.text = "";
            this.newReview.rating = 0;
        },
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