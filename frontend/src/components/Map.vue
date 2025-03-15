<template>
  <div class="map-container">
    <div id="floating-panel">
      <b>Start: </b>
      <input type="text" v-model="startLocation" class="input-field" placeholder="Enter start location">
      <button @click="handleGetCurrentLocation" class="location-btn">Use Current Location</button>
      <b>End: </b>
      <input type="text" v-model="endLocation" class="input-field" placeholder="Enter destination">
      <button @click="getDirections">Get Directions</button>
    </div>
    <div id="map" ref="mapRef"></div>
  </div>
</template>

<script>
import APIService from '../APIService.js';

export default {
  name: 'GoogleMapDirections',
  data() {
    return {
      map: null,
      directionsService: null,
      directionsDisplay: null,
      startLocation: 'NTU',
      endLocation: 'NUS',
      apiKey: ''
    }
  },
  mounted() {
    // Load Google Maps API script dynamically
    if (!window.google) {
      const script = document.createElement('script');
      script.src = `https://maps.googleapis.com/maps/api/js?key=${this.apiKey}`;
      script.async = true;
      script.defer = true;
      script.onload = () => {
        this.initMap();
      };
      document.head.appendChild(script);
    } else {
      // If Google Maps API is already loaded
      this.initMap();
    }
  },
  methods: {
    initMap() {
      // Initialize the Google Maps objects
      // eslint-disable-next-line no-undef
      this.directionsService = new google.maps.DirectionsService();
      // eslint-disable-next-line no-undef
      this.directionsDisplay = new google.maps.DirectionsRenderer();
      
      // Create the map
      // eslint-disable-next-line no-undef
      this.map = new google.maps.Map(this.$refs.mapRef, {
        zoom: 7,
        center: { lat: 41.85, lng: -87.65 }
      });
      
      // Set the map for the DirectionsRenderer
      this.directionsDisplay.setMap(this.map);
      
      // Calculate initial directions
      this.calculateAndDisplayRoute();
    },
    getDirections() {
      this.calculateAndDisplayRoute();
    },
    calculateAndDisplayRoute() {
      if (!this.directionsService || !this.directionsDisplay) return;
      
      this.directionsService.route({
        origin: this.startLocation,
        destination: this.endLocation,
        travelMode: 'DRIVING'
      }, (response, status) => {
        if (status === 'OK') {
          this.directionsDisplay.setDirections(response);
        } else {
          console.error('Directions request failed due to ' + status);
          // You can replace this with a more Vue-friendly notification
          // this.$emit('error', 'Directions request failed due to ' + status);
        }
      });
    },

    handleGetCurrentLocation() {
  // The getCurrentLocation method returns a Promise
  APIService.getCurrentLocation()
    .then(locationInfo => {
      // This code runs AFTER the API call completes successfully
      console.log('Received location:', locationInfo);
      // Format the location string and update the startLocation
      this.startLocation = `${locationInfo.latitude}, ${locationInfo.longitude}`;
    })
    .catch(error => {
      console.error('Error getting current location:', error);
      alert('Unable to retrieve your location. Please check API connection.');
    });
}
  }
}
</script>

<style scoped>
.map-container {
  position: relative;
  height: 600px; /* Adjust as needed */
  width: 100%;
}

#map {
  height: 100%;
  width: 100%;
}

#floating-panel {
  position: absolute;
  top: 10px;
  left: 25%;
  z-index: 5;
  background-color: #fff;
  padding: 5px;
  border: 1px solid #999;
  text-align: center;
  font-family: 'Roboto', 'sans-serif';
  line-height: 30px;
  padding-left: 10px;
}

.input-field {
  margin: 0 5px;
  padding: 5px;
  width: 200px;
  font-family: 'Roboto', 'sans-serif';
}

button {
  background-color: #4285F4;
  color: white;
  border: none;
  padding: 5px 10px;
  margin-left: 5px;
  cursor: pointer;
  font-family: 'Roboto', 'sans-serif';
}

button:hover {
  background-color: #3367D6;
}
</style>