import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import api from '@/api/axios'

export const useAuthStore = defineStore('auth', () => {
  const router = useRouter()

  const token = ref(localStorage.getItem('token'))
  const username = ref(localStorage.getItem('username'))

  const isAuth = computed(() => !!token.value)

  async function login(credentials) {
    try {
      const { data } = await api.post('/auth/login', credentials)
      _setSession(data.username, data.jwt_token)
      router.push('/')
    } catch (e) {
      throw new Error(e.response?.data?.detail ?? 'Ошибка входа', { cause: e })
    }
  }

  async function signup(credentials) {
    try {
      const { data } = await api.post('/auth/signup', credentials)
      
      _setSession(data.username, data.jwt_token)
      router.push('/')
    } catch (e) {
      throw new Error(e.response?.data?.detail ?? 'Ошибка регистрации', { cause: e })
    }
  }

  function logout() {
    token.value = null
    username.value = null
    localStorage.removeItem('token')
    localStorage.removeItem('username')
    router.push('/login')
  }

  function _setSession(u, t) {
    token.value = t
    username.value = u
    console.log(token, username)
    localStorage.setItem('token', t)
    localStorage.setItem('username', u)
    console.log(t)
  }

  
  return { token, username, isAuth, login, signup, logout }
})
