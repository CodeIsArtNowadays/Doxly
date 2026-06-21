<script setup>
import { RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const auth = useAuthStore()
</script>

<template>
  <header
    class="w-full px-8 py-3 flex items-center justify-between"
    style="background-color: #ffffff; border-bottom: 2px solid #BB080B; box-shadow: 0 1px 6px rgba(187,8,11,0.08);"
  >
    <RouterLink to="/" class="flex items-center gap-2 no-underline">
      <div
        class="w-8 h-8 flex items-center justify-center rounded-sm text-white text-xs font-black"
        style="background-color: #BB080B;"
      >
        WS
      </div>
      <span class="text-lg font-bold tracking-tight" style="color: #1A1A1A;">
        Work<span style="color: #BB080B;">Space</span>
      </span>
    </RouterLink>

    <div class="flex items-center gap-3">
      <template v-if="!auth.isAuth">
        <RouterLink to="/login">
          <button
            class="px-5 py-2 rounded text-sm font-semibold text-white hover:opacity-90"
            style="background-color: #BB080B;"
          >
            Войти
          </button>
        </RouterLink>
      </template>

      <template v-else>
        <div class="flex items-center gap-2 px-3 py-1.5 rounded" style="background-color: #F5F5F5;">
          <div
            class="w-6 h-6 rounded-full flex items-center justify-center text-white text-xs font-bold"
            style="background-color: #BB080B;"
          >
            {{ auth.username?.charAt(0).toUpperCase() }}
          </div>
          <span class="text-sm font-medium" style="color: #1A1A1A;">{{ auth.username }}</span>
        </div>

        <button
          @click="auth.logout"
          class="px-4 py-2 rounded text-sm font-medium hover:opacity-80"
          style="border: 1.5px solid #BB080B; color: #BB080B; background: transparent;"
        >
          Выйти
        </button>
      </template>
    </div>
  </header>
</template>
