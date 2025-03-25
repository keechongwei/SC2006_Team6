<template>
  <div class="min-h-screen bg-gradient-to-b from-blue-50 to-blue-100 px-4 py-10">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-3xl md:text-4xl font-extrabold text-center text-blue-900 mb-3">Explore Institutions in Singapore</h1>
      <p class="text-center text-gray-700 text-lg mb-10">
        Navigate Singapore’s diverse education landscape—from foundational to world-class institutions.
      </p>

      <div class="space-y-6">
        <!-- Schools -->
        <div class="bg-white rounded-2xl shadow-md p-6 flex flex-col md:flex-row items-center md:items-start">
          <div class="text-4xl mr-4">🏫</div>
          <div class="flex-1">
            <h2 class="text-xl font-bold text-blue-900 mb-1">Schools</h2>
            <p class="text-gray-700 mb-3">Explore top primary and secondary schools across Singapore, offering strong foundational education.</p>
            <router-link
              to="/schools"
              class="inline-block bg-blue-600 text-white px-5 py-2 rounded-xl font-semibold hover:bg-blue-700 transition"
            >
              View All Primary & Secondary Schools →
            </router-link>
          </div>
        </div>

        <!-- Post-Secondary -->
        <div class="bg-white rounded-2xl shadow-md p-6 flex flex-col md:flex-row items-center md:items-start">
          <div class="text-4xl mr-4">🎓</div>
          <div class="flex-1">
            <h2 class="text-xl font-bold text-blue-900 mb-1">Post-Secondary Institutions</h2>
            <p class="text-gray-700 mb-3">Discover Singapore’s best polytechnics and ITE colleges with career-ready diploma programmes.</p>
            <router-link
              to="/post-secondary"
              class="inline-block bg-blue-600 text-white px-5 py-2 rounded-xl font-semibold hover:bg-blue-700 transition"
            >
              View All Post-Secondary Institutions →
            </router-link>
          </div>
        </div>

        <!-- Specialised -->
        <div class="bg-white rounded-2xl shadow-md p-6 flex flex-col md:flex-row items-center md:items-start">
          <div class="text-4xl mr-4">🎨</div>
          <div class="flex-1">
            <h2 class="text-xl font-bold text-blue-900 mb-1">Specialised Schools</h2>
            <p class="text-gray-700 mb-3">Pursue focused education in arts, sports, or sciences at Singapore’s renowned specialised institutions.</p>
            <router-link
              to="/specialised"
              class="inline-block bg-blue-600 text-white px-5 py-2 rounded-xl font-semibold hover:bg-blue-700 transition"
            >
              View All Specialised Schools →
            </router-link>
          </div>
        </div>

        <!-- Universities -->
        <div class="bg-white rounded-2xl shadow-md p-6 flex flex-col md:flex-row items-center md:items-start">
          <div class="text-4xl mr-4">🎓</div>
          <div class="flex-1">
            <h2 class="text-xl font-bold text-blue-900 mb-1">Universities</h2>
            <p class="text-gray-700 mb-3">Browse world-renowned universities and their top programmes, ranked among Asia’s best.</p>
            <router-link
              to="/universities"
              class="inline-block bg-blue-600 text-white px-5 py-2 rounded-xl font-semibold hover:bg-blue-700 transition"
            >
              View All Universities →
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InstitutionPage',
};
</script>
