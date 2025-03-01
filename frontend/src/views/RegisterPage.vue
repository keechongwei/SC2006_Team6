<template>
    <div>
      <h2>Account Registration</h2>
      <p>Key In Your Username and Password</p>
      <form @submit.prevent="registerUser">
        <input v-model="username" placeholder="Username" required />
        <input v-model="email" type="email" placeholder="Email" required />
        <input v-model="password" type="password" placeholder="Password" required />
        <input v-model="passwordVerify" type="password" placeholder="Re-enter Password" required />
        <button type ="button" @click="$router.push('/login')">Go Back To Login Page</button>
        <button type="submit">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  import axios from "axios";
  
  export default {
    name: "RegistrationPage",
    setup() {
      const username = ref("");
      const email = ref("");
      const password = ref("");
      const passwordVerify = ref("");
  
      const registerUser = async () => {
        if (password.value !== passwordVerify.value) {
          alert("Passwords do not match!");
          return;
        }
  
        try {
          const response = await axios.post("http://127.0.0.1:5000/register", {
            username: username.value,
            email: email.value,
            password: password.value,
          });
  
          alert(response.data.message);
        } catch (error) {
          alert("Registration failed: " + (error.response?.data?.message || "Unknown error"));
        }
      };
  
      return { username, email, password, passwordVerify, registerUser };
    },
  };
  </script>
  