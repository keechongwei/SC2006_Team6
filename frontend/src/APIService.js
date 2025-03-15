import axios from 'axios';

export default class ApiService {
    static async getCurrentLocation() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/location/get_current_location');
        
        // The data is already in JSON format
        const locationData = response.data;
        
        console.log('Location data:', locationData);
        // You can access individual coordinates
        console.log(`Latitude: ${locationData.latitude}`);
        console.log(`Longitude: ${locationData.longitude}`);
        
        return locationData;
      } catch (error) {
        console.error('Error fetching location:', error);
        throw error;
      }
    }
  }