<template>
    <div class="review-section">
      <!-- Review Form -->
      <form v-if="isLoggedIn && !hasLeftReview" @submit.prevent="submitReview">
        <textarea
          v-model="newReview.text"
          placeholder="Leave a review..."
          required
        ></textarea>
        <select v-model="newReview.rating" required>
          <option disabled value="0">Select Rating</option>
          <option v-for="star in 5" :value="star" :key="star">{{ star }} Stars</option>
        </select>
        <button type="submit">Submit</button>
      </form>
      <p v-else-if="!isLoggedIn">
        Please <router-link to="/login">Log In</router-link> to leave a review.
      </p>
      <span v-else></span>
      
  
      <!-- Reviews List -->
      <ul v-if="reviews.length > 0" style="list-style-type: none; padding: 0;">
        <li v-for="review in reviews" :key="review.rid">
          <div>
            <b><router-link :to="'/profile/'+review.uid">{{ review.username }}</router-link></b>
            <span class="simpleBox">
              <span v-for="n in 5" :key="n" :class="{ yellowStar: n <= review.rating }">
                ★
              </span>
            </span>
          </div>
          <blockquote>{{ review.comment }}</blockquote>
          <p class="review-date">{{ review.date }}</p>
          <hr>
        </li>
      </ul>
      <p v-else>No reviews yet. Be the first to review!</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      movieId: {
        type: Number,
        required: true, // Ensure `movieId` is passed correctly
      },
    },
    data() {
      return {
        isLoggedIn: !!localStorage.getItem("userId"),
        hasLeftReview: true,
        newReview: {
          text: "",
          rating: 0,
        },
        reviews: [], // List of reviews
      };
    },
    mounted() {
      this.fetchReviews(); // Fetch reviews on component mount
      this.checkIfUserLeftReview();
    },
    methods: {
      async fetchReviews() {
        try {
          const response = await fetch(`http://127.0.0.1:5000/reviews/movie/${this.movieId}`);
          if (response.ok) {
            const reviewsData = await response.json();
            this.reviews = reviewsData; // Assign fetched reviews to the data property
          } else {
            console.error("Failed to fetch reviews.");
          }
        } catch (error) {
          console.error("Error fetching reviews:", error);
        }
      },
      async checkIfUserLeftReview(){
        const userId = localStorage.getItem("userId");
        try {
          const response = await fetch(`http://127.0.0.1:5000/reviews/validate_review/${userId}/${this.movieId}`);
          const data = await response.json();
          if(data.result == true){
            this.hasLeftReview = true;
          } else {this.hasLeftReview = false;}
          
        } catch (error) {
          console.error("Error checking review status:", error);
        }
      },
      async submitReview() {
        try {
          const userId = localStorage.getItem("userId");
          if (!userId) {
            alert("You must be logged in to submit a review.");
            return;
          }
  
          const response = await fetch(`http://127.0.0.1:5000/reviews/add`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              uid: parseInt(userId),
              mid: this.movieId,
              comment: this.newReview.text,
              rating: this.newReview.rating,
            }),
          });
  
          if (response.ok) {
            const newReview = await response.json();
            this.reviews.push(newReview); // Dynamically add the new review to the list
            this.newReview.text = ""; // Clear the text box
            this.newReview.rating = 0; // Reset the rating
            this.hasLeftReview = true;
            this.fetchReviews(); // Refresh reviews to ensure consistency
          } else {
            console.error("Failed to submit review.");
          }
        } catch (error) {
          console.error("Error submitting review:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .review-date {
    font-size: 0.9rem;
    color: gray;
  }
  
  .simpleBox {
    display: inline-block;
    margin-left: 0.5rem;
  }
  
  .yellowStar {
    color: gold;
  }
  
  textarea {
    width: 100%;
    height: 100px;
    margin-bottom: 1rem;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 5px;
    resize: none;
  }
  
  select {
    margin-bottom: 1rem;
  }
  
  button {
    background-color: #4caf50;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    cursor: pointer;
    font-size: 1rem;
    border-radius: 5px;
  }
  
  button:hover {
    background-color: #45a049;
  }
  </style>
  