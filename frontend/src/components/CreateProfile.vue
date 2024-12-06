<template>
    <NavBar />
    <div class="create-profile">

      <h1>Create Your Profile</h1>
      <form @submit.prevent="handleRegister">
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" id="username" v-model="username" placeholder="Enter your username" required />
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" placeholder="Enter your password" required />
        </div>
        <div class="form-group">
          <label for="bio">Bio</label>
          <textarea id="bio" v-model="bio" placeholder="Tell us about yourself..." required></textarea>
        </div>
        <button type="submit">Create Profile</button>
      </form>
      <p>
        Already have an account? 
        <router-link to="/login">Log In</router-link>
      </p>
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
        password: "",
        bio: "",
      };
    },
    methods: {
      async handleRegister() {
        try {
          const response = await fetch("http://127.0.0.1:5000/users/register", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              username: this.username,
              password: this.password,
              bio: this.bio,
            }),
          });
  
          if (response.ok) {
            alert("Profile created successfully! Please log in.");
            this.$router.push("/login");
          } else {
            const errorData = await response.json();
            alert(`Error: ${errorData.message}`);
          }
        } catch (error) {
          console.error("Failed to create profile:", error);
          alert("An error occurred. Please try again later.");
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add styles for the form */
  form {
    max-width: 400px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  input, textarea {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  button {
    background-color: #4caf50;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  button:hover {
    background-color: #45a049;
  }
  </style>
  