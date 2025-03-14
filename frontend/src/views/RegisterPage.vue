<template>
  <div>
    <h2>Account Registration</h2>
    <p>Key In Your Details</p>
    <form @submit.prevent="registerUser">
      <input v-model="username" placeholder="Username" required />
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <input v-model="passwordVerify" type="password" placeholder="Re-enter Password" required />
      <input v-model.number="age" type="number" placeholder="Age" required />
      
      <label>
        <input type="checkbox" v-model="isStudent" />
        Are you a student?
      </label>

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
  const username = ref("");  // Updated from username to match backend
  const email = ref("");
  const password = ref("");
  const passwordVerify = ref("");
  const age = ref("");  // New field for age
  const isStudent = ref(true);  // Checkbox input for student status

  const registerUser = async () => {
    if (password.value !== passwordVerify.value) {
      alert("Passwords do not match!");
      return;
    }

    try {
      const response = await axios.post("http://127.0.0.1:5000/register", {
        username: username.value,  // Ensure the correct field name
        email: email.value,
        password: password.value,
        age: age.value,  // Include age field
        is_student: isStudent.value,  // Boolean value
      });

      alert(response.data.message || "Registration Successful!");
    } catch (error) {
      alert("Registration failed: " + (error.response?.data?.message || "Unknown error"));
    }
  };

  return { username, email, password, passwordVerify, age, isStudent, registerUser };
},
};
</script>
