<template>
    <div class="login">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <input v-model="username" placeholder="name" required />
        <input v-model="password" type="password" placeholder="Password" required />
        <button type="submit"> Login </button>
        <router-link to="/register">
        <button>Register</button>
        </router-link>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return { username: '', password: '' };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('http://127.0.0.1:5000/login', {
            username: this.username,
            password: this.password,
          });
          alert(response.data.message);
        } catch (error) {
          console.error("Login Error Trace:", error);  // ✅ Print full error trace to console

          // Check if error response exists and extract message
          const errorMessage =
            error.response?.data?.message || "An unknown error occurred";

          alert("Login failed: " + errorMessage);
        }
      },
    },
  };
  </script>
  