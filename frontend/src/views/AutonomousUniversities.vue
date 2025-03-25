<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-white py-10 px-4 sm:px-8">
    <h1 class="text-3xl sm:text-4xl font-bold text-center text-blue-900 mb-4">
      Autonomous Universities
    </h1>
    <p class="text-center text-gray-600 max-w-3xl mx-auto mb-10">
      Explore the unique strengths and offerings of Singapore's Autonomous Universities.
    </p>

    <div class="grid gap-8 max-w-5xl mx-auto">

      <a
        v-for="uni in universities"
        :key="uni.name"
        :href="uni.url"
        target="_blank"
        rel="noopener noreferrer"
        class="block bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition-all border-l-4 border-blue-600 hover:bg-blue-50"
      >
        <div class="flex items-center gap-4">
          <img
            :src="require(`@/assets/${uni.logo}`)"
            :alt="uni.name"
            class="w-16 h-16 object-contain rounded bg-white p-1"
          />
          <h2 class="text-2xl font-semibold text-blue-800">{{ uni.name }}</h2>
        </div>
        <p class="text-gray-700 mt-2">{{ uni.description }}</p>
      </a>

    </div>
  </div>
</template>

<script>
export default {
  name: 'AutonomousUniversities',
  data() {
    return {
      universities: [
        {
          name: 'National University of Singapore (NUS)',
          logo: 'NUS.png',
          url: 'https://nus.edu.sg',
          description:
            'Strong in engineering, medicine, law and business. Offers wide-ranging undergraduate to PhD programs with global partnerships.'
        },
        {
          name: 'Nanyang Technological University (NTU)',
          logo: 'NTU.png',
          url: 'https://ntu.edu.sg',
          description:
            'Leader in engineering, AI and education. Features a smart campus, interdisciplinary learning and global collaborations.'
        },
        {
          name: 'Singapore Management University (SMU)',
          logo: 'SMU.svg',
          url: 'https://smu.edu.sg',
          description:
            'Focused on business, law and computing. Known for seminar-style learning and strong industry engagement.'
        },
        {
          name: 'Singapore University of Technology and Design (SUTD)',
          logo: 'SUTD.png',
          url: 'https://sutd.edu.sg',
          description:
            'Design and innovation focused. Offers interdisciplinary programs in tech, design, architecture and AI.'
        },
        {
          name: 'Singapore Institute of Technology (SIT)',
          logo: 'SIT.png',
          url: 'https://sit.edu.sg',
          description:
            'Applied learning university offering work-study pathways and industry-focused degrees in partnership with overseas institutions.'
        },
        {
          name: 'Singapore University of Social Sciences (SUSS)',
          logo: 'SUSS.png',
          url: 'https://suss.edu.sg',
          description:
            'Specialises in applied social sciences, lifelong learning, and education for adult learners and professionals.'
        }
      ]
    };
  }
};
</script>

<style scoped>
img {
  background: white;
  border-radius: 0.5rem;
  padding: 0.25rem;
}
</style>
