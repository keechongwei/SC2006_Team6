// src/views/SpecialisedPage.vue
<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-white py-10 px-4 sm:px-8">
    <h1 class="text-3xl sm:text-4xl font-bold text-center text-blue-900 mb-4">
      Specialised Schools
    </h1>
    <p class="text-center text-gray-600 max-w-2xl mx-auto mb-10">
      Discover Singapore’s unique specialised schools designed for students with specific interests, talents, or learning needs. These institutions provide tailored education that nurtures personal growth and excellence beyond traditional academic paths.
    </p>

    <div class="flex flex-col gap-6 max-w-3xl mx-auto">
      <router-link to="/specialised/independent" class="block">
        <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition-all border-l-4 border-blue-600">
          <h2 class="text-xl font-semibold text-blue-700">🎭 Specialised Independent Schools</h2>
          <p class="text-sm text-gray-700 mt-2">
            Focus on areas like arts, science, or sports.<br>
            Offer holistic education for talented students in non-traditional disciplines.
          </p>
        </div>
      </router-link>

      <router-link to="/specialised/sped" class="block">
        <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition-all border-l-4 border-blue-600">
          <h2 class="text-xl font-semibold text-blue-700">🧩 Special Education (SPED) Schools</h2>
          <p class="text-sm text-gray-700 mt-2">
            Designed for students with special needs.<br>
            Provide customised support and inclusive learning environments.
          </p>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SpecialisedPage'
}
</script>
