<template>
  <h2> this is the default page for testing other pages</h2>
  <div>
    <nav>
      <router-link to="/">Home</router-link> | 
      <router-link to="/login">Login</router-link> |
      <router-link to="/register">Register</router-link> |
      <router-link to="/Institution">Institution</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>



<style>
/* Add any global styles here */
</style>
