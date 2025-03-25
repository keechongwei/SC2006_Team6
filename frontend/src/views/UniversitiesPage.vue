// src/views/UniversitiesPage.vue
<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-white py-10 px-4 sm:px-8">
    <h1 class="text-3xl sm:text-4xl font-bold text-center text-blue-900 mb-4">
      Universities
    </h1>
    <p class="text-center text-gray-600 max-w-2xl mx-auto mb-10">
      Discover Singapore's higher education landscape—comprising globally respected autonomous universities and versatile private education institutions.
    </p>

    <div class="flex flex-col gap-6 max-w-3xl mx-auto">
      <router-link to="/universities/autonomous" class="block">
        <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition-all border-l-4 border-blue-600">
          <h2 class="text-xl font-semibold text-blue-700">🏛️ Autonomous Universities</h2>
          <p class="text-sm text-gray-700 mt-2">
            Publicly funded institutions offering undergraduate to postgraduate programmes.<br>
            Known for academic excellence and research ecosystems.
          </p>
        </div>
      </router-link>

      <router-link to="/universities/pei" class="block">
        <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition-all border-l-4 border-blue-600">
          <h2 class="text-xl font-semibold text-blue-700">🏫 Private Education Institutions (PEIs)</h2>
          <p class="text-sm text-gray-700 mt-2">
            Offer degrees through international partnerships, enabling flexible pathways into professional careers and higher education.
          </p>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UniversitiesPage'
}
</script>
