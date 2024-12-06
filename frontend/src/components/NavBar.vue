<template>
  <nav class="navbar">
    <div class="nav-left">
      <!-- Home Button/Icon -->
      <router-link to="/" class="home-icon">fIMDB</router-link>
    </div>
    <div><SearchBar class="nav-center" style="margin: auto;" @new-page="$emit('new-page')"/></div>
    <div class="nav-right">
      <div v-if="isLoggedIn">
        <!-- Display Welcome Message, Username (as a Link), and Logout Button -->
        <div class="username-style">
          Welcome, 
          <router-link :to="'/profile/' + uid" class="username-link">{{ username }}</router-link>
        </div>
        <button @click="handleLogout">Logout</button>
      </div>
      <div v-else>
        <!-- Login Button -->
        <button @click="handleLogin">Login</button>
      </div>
    </div>
  </nav>
</template>

<script>
import SearchBar from './SearchBar.vue';
export default {
  data() {
    return {
      isLoggedIn: !!localStorage.getItem("userId"), // Check login status from localStorage
      username: "", // Store the username
      uid: -1,
    };
  },
  components: {
    SearchBar,
  },
  methods: {
    handleLogin() {
      // Redirect to the login page
      this.$router.push("/login");
    },
    handleLogout() {
      // Perform logout logic
      localStorage.removeItem("userId"); // Remove stored userId
      this.isLoggedIn = false; // Update login status
      this.username = ""; // Clear the username
      this.uid = -1;
      this.$router.go(0);
    },
    async fetchUsername() {
      try {
        const userId = localStorage.getItem("userId");
        if (userId) {
          // Fetch username from the backend
          const response = await fetch(`http://127.0.0.1:5000/users/${userId}`);
          if (response.ok) {
            const data = await response.json();
            this.username = data.username;
            this.uid = data.uid;
            this.isLoggedIn = true;
          } else {
            // If the response isn't OK, clear login status
            this.isLoggedIn = false;
            this.uid = -1;
            this.username = "";
          }
        } else {
          // If there's no userId in localStorage
          this.isLoggedIn = false;
          this.uid = -1;
          this.username = "";
        }
      } catch (error) {
        console.error("Failed to fetch username:", error);
        this.isLoggedIn = false;
      }
    },
  },
  mounted() {
    this.fetchUsername(); // Fetch username when the component mounts
  },
};
</script>

<style scoped>
.navbar {
  /* display: flex;
  justify-content: space-between;
  align-items: center; */
  display: grid;
  grid-template-columns: .6fr 20fr 1.5fr;
  padding: 0.5rem 1rem;
  background-color: #4caf50; 
  color: white;
}

.nav-left .home-icon {
  font-size: 1.5rem;
  font-weight: bold;
  text-decoration: none;
  color: white;
}

.nav-center {
  text-align: center;
}
.nav-right username-style {
  padding-right: 100rem;
}
.nav-right button {
  background-color: white;
  color: #4caf50;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  font-size: 1rem;
  border-radius: 5px;
  margin-left: 12px;
}

.nav-right button:hover {
  background-color: #45a049;
  color: white;
}

.username-link {
  text-decoration: underline;
  color: white;
  cursor: pointer;
}

.username-link:hover {
  color: #ffcc00; /* Change hover color for username link */
}
</style>
