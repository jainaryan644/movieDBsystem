<template>
    <div class="review-section">
      <!-- Review Form -->
      <form v-if="isLoggedIn" @submit.prevent="submitReview">
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
      <p v-else>
        Please <router-link to="/login">Log In</router-link> To Leave a Review
      </p>
  
      <!-- Reviews List -->
      <ul style="list-style-type: none; padding: 0;">
        <li v-for="review in reviews" :key="review.id">
          <div>
            <b>{{ review.username }}</b> 
            <span class="simpleBox">
              <span v-for="n in 5" :key="n" :class="{ yellowStar: n <= review.rating }">
                ★
              </span>
            </span>
          </div>
          <blockquote>{{ review.comment }}</blockquote>
        </li>
      </ul>
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
        username: "",
        newReview: {
          text: "",
          rating: 0,
        },
        reviews: [],
      };
    },
    mounted() {
      this.fetchReviews(); // Fetch reviews when component is mounted
      this.fetchUsername(); // Fetch username if logged in
    },
    methods: {
      async fetchUsername() {
        try {
          const userId = localStorage.getItem("userId");
          if (userId) {
            const response = await fetch(`http://127.0.0.1:5000/users/${userId}`);
            if (response.ok) {
              const data = await response.json();
              this.username = data.username;
              this.isLoggedIn = true;
            } else {
              this.isLoggedIn = false;
              this.username = "";
            }
          }
        } catch (error) {
          console.error("Failed to fetch username:", error);
        }
      },
      async fetchReviews() {
        try {
          const response = await fetch(`http://127.0.0.1:5000/reviews/${this.movieId}`);
          if (response.ok) {
            this.reviews = await response.json();
          } else {
            console.error("Failed to fetch reviews.");
          }
        } catch (error) {
          console.error("Error fetching reviews:", error);
        }
      },
      async submitReview() {
        try {
          const userId = localStorage.getItem("userId");
          if (!userId) {
            alert("You must be logged in to submit a review.");
            return;
          }
  
          const response = await fetch(`http://127.0.0.1:5000/reviews`, {
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
            // Add new review to list dynamically
            const addedReview = await response.json();
            this.reviews.push(addedReview);
  
            // Reset form
            this.newReview.text = "";
            this.newReview.rating = 0;
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
  