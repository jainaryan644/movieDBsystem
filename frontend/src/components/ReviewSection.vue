<template>
  <div class="review-section">
    <h2>Reviews</h2>

    <!-- Review Form -->
    <form v-if="isLoggedIn && !hasLeftReview" @submit.prevent="submitReview">
      <textarea
        v-model="newReview.comment"
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
    <p v-else>
      You have already left a review for this movie.
    </p>

    <!-- Reviews List -->
    <ul style="list-style-type: none; padding: 0;">
      <li v-for="review in reviews" :key="review.rid">
        <div>
          <b>
            <router-link :to="'/profile/' + review.uid" class="user-link">
              {{ review.username }}
            </router-link>
          </b>
          <span class="simpleBox">
            <span
              v-for="n in 5"
              :key="n"
              :class="{ yellowStar: n <= review.rating }"
            >
              ★
            </span>
          </span>
        </div>
        <blockquote>{{ review.comment }}</blockquote>
        <div>
          <button
            :disabled="!isLoggedIn || review.userVoted === 'upvote'"
            @click="vote(review.rid, 'upvote')"
            class="vote-button"
          >
            👍 
          </button>
          <span class="net-votes">{{ review.netVotes }}</span>
          <button
            :disabled="!isLoggedIn || review.userVoted === 'downvote'"
            @click="vote(review.rid, 'downvote')"
            class="vote-button"
          >
            👎 
          </button>
        </div>
        <p class="review-date">{{ review.date }}</p>
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
        hasLeftReview: false, // Check if the user has already left a review
        username: "",
        newReview: {
          comment: "",
          rating: 0,
        },
        reviews: [],
      };
    },
    mounted() {
      this.fetchReviews(); // Fetch reviews when component is mounted
      this.fetchUsername(); // Fetch username if logged in
      this.checkIfUserLeftReview(); // Check if the user has already reviewed this movie
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
              console.error("Failed to fetch reviews.");
            }
          }
        } catch (error) {
          console.error("Error fetching reviews:", error);
        }
      },
      async fetchReviews() {
        try {
          const response = await fetch(
            `http://127.0.0.1:5000/reviews/movie/${this.movieId}`
          );
          if (response.ok) {
            this.reviews = await response.json();
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
      async vote(reviewId, voteType) {
        const userId = localStorage.getItem("userId");
        if (!userId) {
          alert("You must be logged in to vote!");
          return;
        }

        try {
          const response = await fetch(`http://127.0.0.1:5000/reviews/vote`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              user_id: parseInt(userId),
              review_id: reviewId,
              vote_type: voteType,
            }),
          });

          if (response.ok) {
            const data = await response.json();
            const index = this.reviews.findIndex((r) => r.rid === reviewId);
            if (index !== -1) {
              this.reviews[index].netVotes = data.net_votes; // Update net votes dynamically
              this.reviews[index].userVoted = voteType; // Mark which vote was cast
            }
          } else {
            console.error("Failed to submit vote.");
          }
        } catch (error) {
          console.error("Error submitting vote:", error);
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
  
  .user-link {
    color: black;
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
  