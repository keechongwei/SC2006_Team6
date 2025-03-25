// src/views/SchoolsPage.vue
<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-white py-10 px-4 sm:px-8">
    <h1 class="text-3xl sm:text-4xl font-bold text-center text-blue-900 mb-4">
      Schools
    </h1>
    <p class="text-center text-gray-600 max-w-2xl mx-auto mb-10">
      Navigate Singapore's foundational education system—from primary schools nurturing early learners to secondary schools shaping students for the next academic leap.
    </p>

    <div class="flex flex-col gap-6 max-w-3xl mx-auto">
      <router-link to="/schools/primary" class="block">
        <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition-all border-l-4 border-blue-600">
          <h2 class="text-xl font-semibold text-blue-700">📖 Primary Schools
          </h2>
          <p class="text-sm text-gray-700 mt-2">
            Ages: <strong>7–12</strong> (Primary 1–6)<br>
            Culminates with: <strong>PSLE (Primary School Leaving Examination)</strong><br>
            Lays the academic and character foundation of every student’s journey.
          </p>
        </div>
      </router-link>

      <router-link to="/schools/secondary" class="block">
        <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition-all border-l-4 border-blue-600">
          <h2 class="text-xl font-semibold text-blue-700">📗 Secondary Schools
          </h2>
          <p class="text-sm text-gray-700 mt-2">
            Ages: <strong>13–16/17</strong> (Secondary 1–4/5)<br>
            Academic Streams:
            <ul class="list-disc list-inside">
              <li>Express (O-Level)</li>
              <li>Normal (Academic)</li>
              <li>Normal (Technical)</li>
            </ul>
          </p>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SchoolsPage'
}
</script>
