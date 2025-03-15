<template>
  <div class="institution-page">
    <h1>Institution Details</h1>
    
    <!-- Other institution content goes here -->
    
    <h2>Directions</h2>
    <GoogleMapDirections />
  </div>
</template>

<script>
import GoogleMapDirections from '../components/Map.vue'; // Adjust the path as needed

export default {
  name: 'InstitutionPage',
  components: {
    GoogleMapDirections
  },
  data() {
    return {
      // Your institution data
    }
  },
  methods: {
    // Your methods
  }
}
</script>

<style scoped>
.institution-page {
  padding: 20px;
}
</style>