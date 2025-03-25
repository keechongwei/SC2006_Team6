// src/views/PostSecondaryPage.vue
<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-white py-10 px-4 sm:px-8">
    <h1 class="text-3xl sm:text-4xl font-bold text-center text-blue-900 mb-4">
      Post-Secondary Institutions
    </h1>
    <p class="text-center text-gray-600 max-w-2xl mx-auto mb-10">
      Explore Singapore's post-secondary options designed to prepare students for higher education or the workforce. These institutions offer tailored pathways to support various aspirations and learning styles.
    </p>

    <div class="flex flex-col gap-6 max-w-3xl mx-auto">
      <router-link to="/post-secondary/jc" class="block">
        <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition-all border-l-4 border-blue-600">
          <h2 class="text-xl font-semibold text-blue-700">🎓 Junior Colleges (JC)</h2>
          <p class="text-sm text-gray-700 mt-2">
            Duration: <strong>2 years</strong><br>
            Leads to: <strong>GCE A-Levels</strong><br>
            Prepares for university education.
          </p>
        </div>
      </router-link>

      <router-link to="/post-secondary/mi" class="block">
        <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition-all border-l-4 border-blue-600">
          <h2 class="text-xl font-semibold text-blue-700">🏛️ Millennia Institute (MI)</h2>
          <p class="text-sm text-gray-700 mt-2">
            Duration: <strong>3 years</strong><br>
            Similar to JC but more spread out.<br>
            Offers A-Level curriculum.
          </p>
        </div>
      </router-link>

      <router-link to="/post-secondary/polytechnic" class="block">
        <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition-all border-l-4 border-blue-600">
          <h2 class="text-xl font-semibold text-blue-700">👩‍💻 Polytechnics</h2>
          <p class="text-sm text-gray-700 mt-2">
            Duration: <strong>3 years</strong><br>
            Diplomas in various fields.<br>
            Prepares for workforce or university.
          </p>
        </div>
      </router-link>

      <router-link to="/post-secondary/ite" class="block">
        <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition-all border-l-4 border-blue-600">
          <h2 class="text-xl font-semibold text-blue-700">🛠️ Institute of Technical Education (ITE)</h2>
          <p class="text-sm text-gray-700 mt-2">
            Offers <strong>Nitec</strong> and <strong>Higher Nitec</strong><br>
            Technical and vocational training.
          </p>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostSecondaryPage'
}
</script>
