<template>
  <nav class="navbar">
    <div class="nav-left">
      <!-- Home Button/Icon -->
      <router-link to="/" class="home-icon">fIMDB</router-link>
    </div>
    <div class="nav-right">
      <!-- Login/Logout Button -->
      <button @click="handleAuthAction">
        {{ isLoggedIn ? "Logout" : "Login" }}
      </button>
      <p> {{ isLoggedIn ? "Username" : "" }} </p>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      isLoggedIn: false, // Replace with your authentication logic
    };
  },
  methods: {
    handleAuthAction() {
      if (this.isLoggedIn) {
        // Perform logout logic
        this.isLoggedIn = false; // Update authentication status
        this.$router.push("/login"); // Redirect to login page
      } else {
        // Redirect to login page
        this.$router.push("/login");
      }
    },
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
</style>
