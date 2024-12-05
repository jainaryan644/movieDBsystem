<template>
  <nav class="navbar">
    <div class="nav-left">
      <!-- Home Button/Icon -->
      <router-link to="/" class="home-icon">fIMDB</router-link>
    </div>
    <div class="nav-right">
      <div v-if="isLoggedIn">
        <!-- Display Welcome Message, Username (as a Link), and Logout Button -->
        <span>
          Welcome, 
          <router-link to="/profile" class="username-link">{{ username }}</router-link> 
          | 
        </span>
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
export default {
  data() {
    return {
      isLoggedIn: !!localStorage.getItem("userId"), // Check login status from localStorage
      username: "", // Store the username
    };
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
  },
  mounted() {
    this.fetchUsername(); // Fetch username when the component mounts
  },
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 1rem;
  background-color: #4caf50; /* Adjust color to match your theme */
  color: white;
}

.nav-left .home-icon {
  font-size: 1.5rem;
  font-weight: bold;
  text-decoration: none;
  color: white;
}

.nav-right button {
  background-color: white;
  color: #4caf50;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  font-size: 1rem;
  border-radius: 5px;
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
