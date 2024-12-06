<template>
    <div class="user-profile-page">
      <NavBar />
      <p v-if="$route.params.uid < 1">Not logged in</p>
      <div v-else class="profile-container">
        <div id="profile-title">
          <h1>{{ username }}</h1>
          <button v-if="isUser" @click="routeToSettings">Profile Settings</button>
        </div>
        <h2>Bio</h2>
        <p>{{ userBio }}</p>
        <h2>Reviews</h2>
        <ul v-if="reviews.length > 0" style="list-style-type: none; padding: 0;">
          <li v-for="review in reviews" :key="review.rid">
            <hr>
            <div>
              <b><router-link v-bind:to="'/movie/' + review.movie_mid">{{ review.movie_title }}</router-link></b>
            </div>
            <blockquote>
              <p>{{ review.comment }}</p>
              <div>
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
            </blockquote>
            <p class="review-date">{{ review.date }}</p>
          </li>
          <hr>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import NavBar from "./NavBar.vue";
  
  export default {
    components: {
      NavBar,
    },
    data() {
      return {
        username: "",
        userBio: "",
        reviews: [],
        isUser: false,
      };
    },
    methods: {
      routeToSettings(){
        this.$router.push("/settings");
      },
      async getUserDetails(){
        const userId = this.$route.params.uid;
  
        // Fetch username and bio
        try {
          const response = await fetch(`http://127.0.0.1:5000/users/${userId}`);
          if (response.ok) {
            const data = await response.json();
            this.username = data.username;
            this.userBio = data.bio;
          } else {
            console.error("Failed to fetch user details");
          }
        } catch (error) {
          console.error("Error fetching user details:", error);
        }
      },
      async getUserReviews(){
        const userId = this.$route.params.uid;

        // Fetch user reviews
        try {
          const reviewsResponse = await fetch(
            `http://127.0.0.1:5000/reviews/user/${userId}`
          );
          if (reviewsResponse.ok) {
            const reviewsData = await reviewsResponse.json();
            this.reviews = reviewsData;
          } else {
            console.error("Failed to fetch user reviews");
          }
        } catch (error) {
          console.error("Error fetching user reviews:", error);
        }
      }
    },
    async mounted() {
      this.getUserDetails();
      this.getUserReviews();
      const userId = localStorage.getItem("userId");
      console.log(userId);
      console.log(this.$route.params.uid);
      if(userId == this.$route.params.uid){
        this.isUser = true;
      }
      
    },
  };
  </script>
  
  <style scoped>
  #profile-title {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  h1 {
    margin: 0;
  }
  button {
    margin-left: auto;
  }
  .review-date {
    font-size: 0.9rem;
    color: gray;
  }

  .user-profile-page {
    padding: 1rem;
  }
  
  .profile-container {
    margin: 2rem;
  }
  
  h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }
  
  h2 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
  }
  
  .simpleBox {
    display: inline-block;
  }
  
  .yellowStar {
    color: gold;
  }
  button {
    background-color: #4caf50;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  