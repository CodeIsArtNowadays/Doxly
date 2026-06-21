  import { createRouter, createWebHistory } from 'vue-router'
  import { useAuthStore } from '@/stores/auth'
  import HomeView from '@/views/HomeView.vue'
  import LoginView from '@/views/LoginView.vue'
  import SignupView from '@/views/SignupView.vue'
  import WorkspaceView from '@/views/WorkspaceView.vue'
  
  
  const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
      {
        path: '/',
        name: 'home',
        component: HomeView,
        meta: { requiresAuth: true }
      },
      {
        path: '/login',
        name: 'login',
        component: LoginView,
        meta: { requiresGuest: true }
      },
      {
        path: '/signup',
        name: 'signup',
        component: SignupView,
        meta: { requiresGuest: true }
      },
  
      // Добавь в routes:
      {
        path: '/workspace/:id',
        name: 'workspace',
        component: WorkspaceView,
        meta: { requiresAuth: true }
      }
  
    ],
  })
  
  router.beforeEach((to) => {
    const auth = useAuthStore()
  
    if (to.meta.requiresAuth && !auth.isAuth) {
      return { name: 'login' }
    }
  
    if (to.meta.requiresGuest && auth.isAuth) {
      return { name: 'home' }
    }
  })
  
  export default router
