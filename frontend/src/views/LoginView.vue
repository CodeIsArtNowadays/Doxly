<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const auth = useAuthStore()

const username = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

async function handleLogin() {
  error.value = ''
  loading.value = true
  try {
    await auth.login({ username: username.value, password: password.value })
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center" style="background-color: #F5F5F5;">
    <div
      class="w-full max-w-md rounded-lg overflow-hidden"
      style="background: #FFFFFF; box-shadow: 0 4px 24px rgba(0,0,0,0.10);"
    >

      <!-- Шапка -->
      <div class="px-8 py-6 flex items-center gap-3" style="background-color: #BB080B;">
        <div
          class="w-9 h-9 rounded-sm flex items-center justify-center text-white text-xs font-black"
          style="background-color: rgba(255,255,255,0.2);"
        >
          WS
        </div>
        <div>
          <p class="text-white text-lg font-bold leading-tight">WorkSpace</p>
          <p class="text-xs" style="color: rgba(255,255,255,0.75);">Войдите в аккаунт</p>
        </div>
      </div>

      <!-- Форма -->
      <form @submit.prevent="handleLogin" class="px-8 py-7 flex flex-col gap-5">

        <div
          v-if="error"
          class="px-4 py-3 rounded text-sm font-medium"
          style="background-color: #FFF0F0; border: 1px solid #BB080B; color: #BB080B;"
        >
          {{ error }}
        </div>

        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-semibold uppercase tracking-wider" style="color: #6B6B6B;">
            Имя пользователя
          </label>
          <input
            v-model="username"
            type="text"
            placeholder="eraami_"
            required
            class="w-full px-4 py-2.5 rounded text-sm outline-none"
            style="border: 1.5px solid #E0E0E0; color: #1A1A1A; background: #FAFAFA;"
            @focus="$event.target.style.borderColor = '#BB080B'"
            @blur="$event.target.style.borderColor = '#E0E0E0'"
          />
        </div>

        <div class="flex flex-col gap-1.5">
          <label class="text-xs font-semibold uppercase tracking-wider" style="color: #6B6B6B;">
            Пароль
          </label>
          <input
            v-model="password"
            type="password"
            placeholder="••••••••"
            required
            class="w-full px-4 py-2.5 rounded text-sm outline-none"
            style="border: 1.5px solid #E0E0E0; color: #1A1A1A; background: #FAFAFA;"
            @focus="$event.target.style.borderColor = '#BB080B'"
            @blur="$event.target.style.borderColor = '#E0E0E0'"
          />
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full py-2.5 rounded text-sm font-semibold text-white"
          :style="{
            backgroundColor: '#BB080B',
            opacity: loading ? '0.7' : '1',
            cursor: loading ? 'not-allowed' : 'pointer'
          }"
        >
          {{ loading ? 'Входим...' : 'Войти' }}
        </button>

        <p class="text-center text-sm" style="color: #6B6B6B;">
          Нет аккаунта?
          <RouterLink
            to="/signup"
            class="font-semibold hover:opacity-70"
            style="color: #BB080B;"
          >
            Зарегистрироваться
          </RouterLink>
        </p>

      </form>
    </div>
  </div>
</template>
