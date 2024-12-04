<template>
  <div class="login-page">
    <h1>fiMDB</h1>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" placeholder="Enter your username" />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" placeholder="Enter your password" />
      </div>
      <button type="submit">Login</button>
      <p v-if="error" class="error-message">{{ error }}</p>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      error: null,
    };
  },
  methods: {
    async handleLogin() {
      this.error = null; // Reset any existing errors
      try {
        const response = await fetch("http://127.0.0.1:5000/users/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
          }),
        });

        if (!response.ok) {
          const errorData = await response.json();
          this.error = errorData.message || "Login failed. Please try again.";
          return;
        }

        const data = await response.json();
        console.log("User logged in with UID:", data.uid);

        // Save the user's UID in localStorage or a state management library like Vuex
        localStorage.setItem("userId", data.uid);

        // Redirect to the homepage or dashboard
        this.$router.push("/");
      } catch (error) {
        console.error("Login error:", error);
        this.error = "An error occurred. Please try again later.";
      }
    },
  },
};
</script>

<style scoped>
.error-message {
  color: red;
  margin-top: 1rem;
}
</style>
