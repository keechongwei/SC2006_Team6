<template>
  <div class="min-h-screen bg-gray-50 text-gray-800 font-sans">
    <!-- Header -->
    <header class="bg-white shadow-sm">
      <div class="container mx-auto px-6 py-4 flex justify-between items-center">
        <h1 class="text-2xl font-bold text-blue-600">LearnLeap</h1>
        <nav class="space-x-6 text-sm font-medium text-gray-700">
          <router-link to="/" class="hover:text-blue-500">Home</router-link>
          <router-link to="/login" class="hover:text-blue-500">Login</router-link>
          <router-link to="/register" class="hover:text-blue-500">Register</router-link>
          <router-link to="/institution" class="hover:text-blue-500">Institution</router-link>
        </nav>
      </div>
    </header>

    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-blue-50 to-white py-20">
      <div class="container mx-auto px-6 text-center">
        <h2 class="text-4xl font-extrabold mb-4">Find Your Perfect <span class="text-blue-600">Educational Institution</span></h2>
        <p class="text-gray-600 text-lg mb-8 max-w-2xl mx-auto">
          Discover universities, junior colleges, and schools across Singapore with LearnLeap’s comprehensive search system.
        </p>
        <div class="max-w-xl mx-auto">
          <input
            type="text"
            placeholder="Search by institution name..."
            class="w-full px-6 py-3 border border-gray-300 rounded-full shadow-sm focus:ring-blue-500 focus:border-blue-500"
          />
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-white mt-20 py-6 border-t border-gray-200 text-center text-sm text-gray-500">
      © {{ new Date().getFullYear() }} LearnLeap. All rights reserved.
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

body {
  font-family: 'Inter', sans-serif;
}
</style>
