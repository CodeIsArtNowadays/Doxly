import axios from 'axios'

const api = axios.create({
  baseURL: 'http://139.100.235.44:8001', 
  // baseURL: 'http://localhost:8001', 
  headers: {
    'Content-Type': 'application/json',
  },
})

// Автоматически вставляет токен в каждый запрос
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default api
