<template>
    <NavBar />
    <div class="create-profile">
        <button id="profile-button" @click="routeToProfile">Back To Profile</button>
        <h1>User Settings</h1>
        <h2>User: {{ username }}</h2>
        <form @submit.prevent="handleUpdateBio">
            <div class="form-group">
                <label for="bio">Bio</label>
                <textarea id="bio" v-model="bio" :placeholder="bio" required></textarea>
            </div>
            <button type="submit">Update Bio</button>
        </form>
        <form @submit.prevent="handleUpdatePassword">
            <div class="form-group">
                <label for="New Password">New Password</label>
                <input type="password" id="password" v-model="nPassword" placeholder="Enter new password" required />
                <label for="Current Password">Current Password</label>
                <input type="password" id="password" v-model="cPassword" placeholder="Enter current password" required />
            </div>
            <button type="submit">Update Password</button>
        </form>
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
                bio: "",
                nPassword: "",
                cPassword: "",
            };
        },
        setup(){
            
        },
        mounted(){
            const userId = localStorage.getItem("userId");
            if(!userId){this.$router.push("/login");}
            this.getUserDetails();
        },
        methods: {
            routeToProfile(){
                const userId = localStorage.getItem("userId");
                this.$router.push("/profile/" + userId);
            },
            async getUserDetails(){
                const userId = localStorage.getItem("userId");
    
                // Fetch username and bio
                try {
                    const response = await fetch(`http://127.0.0.1:5000/users/${userId}`);
                    if (response.ok) {
                        const data = await response.json();
                        this.username = data.username;
                        this.bio = data.bio;
                    } else {
                        console.error("Failed to fetch user details");
                    }
                } catch (error) {
                    console.error("Error fetching user details:", error);
                }
            },
            async handleUpdateBio() {
                const userId = localStorage.getItem("userId");
                try {
                    const response = await fetch("http://127.0.0.1:5000/users/update", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            element: "bio",
                            bio: this.bio,
                            uid: userId
                        }),
                    });

                    if (response.ok) {
                        alert("Bio updated successfully!");
                        this.$router.push("/settings");
                    } else {
                        const errorData = await response.json();
                        alert(`Error: ${errorData.message}`);
                    }
                } catch (error) {
                    console.error("Failed to update bio:", error);
                    alert("An error occurred. Please try again later.");
                }
            },
            async handleUpdatePassword() {
                const userId = localStorage.getItem("userId");
                try {
                    const response = await fetch("http://127.0.0.1:5000/users/update", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            element: "password",
                            nPassword: this.nPassword,
                            cPassword: this.cPassword,
                            uid: userId
                        }),
                    });

                    if (response.ok) {
                        alert("Password updated successfully!");
                        this.$router.push("/settings");
                    } else {
                        const errorData = await response.json();
                        alert(`Error: ${errorData.message}`);
                    }
                } catch (error) {
                    console.error("Failed to update bio:", error);
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
  #profile-button{
    margin-bottom: 0.1rem;
    margin-top: 1rem;
  }
  button:hover {
    background-color: #45a049;
  }
  </style>
  