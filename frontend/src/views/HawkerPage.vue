<template>
    <div class="p-6 max-w-4xl mx-auto">
      <h1 class="text-2xl font-bold mb-4">Find Nearby Hawker Centers</h1>
  
      <div class="mb-4">
        <label class="block text-sm font-medium text-gray-700">Latitude:</label>
        <input v-model="latitude" type="text" placeholder="Enter latitude" class="w-full p-2 border rounded-lg" />
      </div>
  
      <div class="mb-4">
        <label class="block text-sm font-medium text-gray-700">Longitude:</label>
        <input v-model="longitude" type="text" placeholder="Enter longitude" class="w-full p-2 border rounded-lg" />
      </div>
  
      <button @click="getCurrentLocation" class="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2">
        Use Current Location
      </button>
      
      <button @click="findNearbyHawkers" class="bg-green-500 text-white px-4 py-2 rounded-lg">
        Find Hawkers
      </button>
  
      <div v-if="hawkerCenters.length" class="mt-6">
        <h2 class="text-lg font-semibold">Nearby Hawker Centers:</h2>
        <ul class="list-disc list-inside mt-2">
          <li v-for="(hawker, index) in hawkerCenters" :key="index">
            {{ hawker.name }} ({{ hawker.distance_km }} km away)
          </li>
        </ul>
      </div>
  
      <div id="map" class="mt-6" style="height: 400px; width: 100%;"></div>
    </div>
  </template>
  
  <script>
  /* global google */
  (g => {
  var h, a, k, 
      p = "The Google Maps JavaScript API",
      c = "google",
      l = "importLibrary",
      q = "__ib__",
      m = document,
      b = window;

  b = b[c] || (b[c] = {});
  var d = b.maps || (b.maps = {}),
      r = new Set,
      e = new URLSearchParams,
      u = () => h || (h = new Promise((f, n) => { // ✅ FIX: Removed async
          a = m.createElement("script");  // ✅ Removed `await`
          e.set("libraries", [...r] + "");
          for (k in g) e.set(k.replace(/[A-Z]/g, t => "_" + t[0].toLowerCase()), g[k]);
          e.set("callback", c + ".maps." + q);
          a.src = `https://maps.${c}apis.com/maps/api/js?` + e;
          d[q] = f;
          a.onerror = function() { h = n(Error(p + " could not load.")); };
          a.nonce = m.querySelector("script[nonce]")?.nonce || "";
          m.head.append(a);
      }));

    d[l] ? console.warn(p + " only loads once. Ignoring:", g) : d[l] = (f, ...n) => r.add(f) && u().then(() => d[l](f, ...n));
    })({
    key: "AIzaSyBD7iBOxLpy3X586aP9ftcJoYDROuCHb1Q",
    v: "weekly",
    // Use the 'v' parameter to indicate the version to use (weekly, beta, alpha, etc.).
    // Add other bootstrap parameters as needed, using camel case.
    });

  import axios from 'axios';
  
  export default {
    data() {
      return {
        latitude: '',
        longitude: '',
        hawkerCenters: [],
        map: null
      };
    },
    methods: {
      async getCurrentLocation() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/api/location/get_current_location');
          if (response.data && response.data.latitude && response.data.longitude) {
            this.latitude = response.data.latitude;
            this.longitude = response.data.longitude;
            this.initializeMap();
          } else {
            alert('Failed to retrieve location.');
          }
        } catch (error) {
          console.error('Error fetching current location:', error);
          alert('Error retrieving location.');
        }
      },
      async findNearbyHawkers() {
        if (!this.latitude || !this.longitude) {
          alert('Please enter latitude and longitude.');
          return;
        }
        try {
          const response = await axios.get('http://127.0.0.1:5000/find-nearby-hawkers', {
            params: { latitude: parseFloat(this.latitude), longitude: parseFloat(this.longitude) }
          });
  
          this.hawkerCenters = response.data.nearby_centres || [];
          this.addHawkerMarkers();
        } catch (error) {
          console.error('Error fetching hawker centers:', error);
          alert('Error retrieving hawker centers.');
        }
      },
      async initializeMap() {
        if (!this.latitude || !this.longitude) return;

        try {
            const position = { lat: parseFloat(this.latitude), lng: parseFloat(this.longitude) };

            const { Map } = await google.maps.importLibrary("maps");
            const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

            this.map = new Map(document.getElementById("map"), {
                zoom: 14,
                center: position,
                mapId: "DEMO_MAP_ID",
            });

            // ✅ Add user location marker
            new AdvancedMarkerElement({
                position: position,
                map: this.map,
                title: "Your Location",
            });

            console.log("Map initialized with user location:", position);
        } catch (error) {
            console.error("Google Maps failed to initialize:", error);
        }
      },
      async addHawkerMarkers() {
        if (!this.map) {
            console.error("Map is not initialized yet.");
            return;
        }

        try {
            const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

            this.hawkerCenters.forEach(hawker => {
                console.log("Adding marker for:", hawker.name, hawker.latitude, hawker.longitude);

                const marker = new AdvancedMarkerElement({
                    position: { lat: parseFloat(hawker.latitude), lng: parseFloat(hawker.longitude) },
                    map: this.map,
                    title: hawker.name,
                });

                console.log("Marker created:", marker);
            });
        } catch (error) {
            console.error("Failed to add hawker markers:", error);
        }
      },
  },
  mounted() {
    this.initializeMap();
  }
};
</script>