import axios from 'axios'

const apiClient= axios.create({
    baseURL: 'http://localhost:8000/api',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json'
    }
});

apiClient.interceptors.response.use(
  (response) => {
    
    return response;
  },
  (error) => {
    if (error.response && error.response.status === 429) {
      console.error("Rate limit exceeded! Please wait before trying again.");
    }
    
    
    return Promise.reject(error);
  }
);

export default apiClient;