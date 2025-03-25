<template>
    <div class="min-h-screen bg-gradient-to-br from-blue-50 to-white py-16 px-6">
      <div class="max-w-5xl mx-auto text-center">
        <h1 class="text-4xl font-extrabold text-blue-900 mb-4">Explore Institutions in Singapore</h1>
        <p class="text-gray-600 text-lg mb-12">
          Navigate Singapore’s diverse education landscape—from foundational to world-class institutions.
        </p>
  
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Schools -->
          <router-link
            to="/schools"
            class="bg-white shadow-xl rounded-xl p-8 hover:shadow-2xl transition border border-gray-200 hover:-translate-y-1 transform duration-200"
          >
            <div class="flex items-center justify-center mb-4">
              <img
                src="https://img.icons8.com/fluency/96/school-building.png"
                alt="Schools"
                class="w-20 h-20"
              />
            </div>
            <h2 class="text-xl font-semibold text-blue-800 mb-2">Schools</h2>
            <p class="text-gray-600">
              Explore top primary and secondary schools across Singapore.
            </p>
          </router-link>
  
          <!-- Polytechnics -->
          <router-link
            to="/polytechnics"
            class="bg-white shadow-xl rounded-xl p-8 hover:shadow-2xl transition border border-gray-200 hover:-translate-y-1 transform duration-200"
          >
            <div class="flex items-center justify-center mb-4">
              <img
                src="https://img.icons8.com/fluency/96/certificate.png"
                alt="Polytechnics"
                class="w-20 h-20"
              />
            </div>
            <h2 class="text-xl font-semibold text-blue-800 mb-2">Polytechnics</h2>
            <p class="text-gray-600">
              Discover Singapore's best polytechnics and diploma courses.
            </p>
          </router-link>
  
          <!-- Universities -->
          <router-link
            to="/universities"
            class="bg-white shadow-xl rounded-xl p-8 hover:shadow-2xl transition border border-gray-200 hover:-translate-y-1 transform duration-200"
          >
            <div class="flex items-center justify-center mb-4">
              <img
                src="https://img.icons8.com/fluency/96/graduation-cap.png"
                alt="Universities"
                class="w-20 h-20"
              />
            </div>
            <h2 class="text-xl font-semibold text-blue-800 mb-2">Universities</h2>
            <p class="text-gray-600">
              Browse world-renowned universities and their top programmes.
            </p>
          </router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'InstitutionPage',
  };
  </script>
  