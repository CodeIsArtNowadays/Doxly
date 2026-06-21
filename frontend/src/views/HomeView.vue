<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import WorkspaceItem from '@/components/WorkspaceItem.vue'
import api from '@/api/axios'

const router = useRouter()

const workspaces = ref([])
const loading = ref(false)
const error = ref('')

// Попап
const showModal = ref(false)
const newTitle = ref('')
const creating = ref(false)
const createError = ref('')

async function fetchWorkspaces() {
  loading.value = true
  try {
    const { data } = await api.get('/')
    workspaces.value = data
  // eslint-disable-next-line no-unused-vars
  } catch (e) {
    error.value = 'Не удалось загрузить воркспейсы'
  } finally {
    loading.value = false
  }
}

function openModal() {
  newTitle.value = ''
  createError.value = ''
  showModal.value = true
}

function closeModal() {
  showModal.value = false
}

async function createWorkspace() {
  if (!newTitle.value.trim()) {
    createError.value = 'Введите название'
    return
  }
  creating.value = true
  createError.value = ''
  try {
    const { data } = await api.post('/', { title: newTitle.value.trim() })
    router.push(`/workspace/${data.id}`)
  // eslint-disable-next-line no-unused-vars
  } catch (e) {
    createError.value = 'Не удалось создать воркспейс'
  } finally {
    creating.value = false
  }
}

onMounted(fetchWorkspaces)
</script>

<template>
  <div class="min-h-screen" style="background-color: #F5F5F5;">

    <!-- Тулбар -->
    <div
      class="w-full px-8 py-3 flex items-center justify-between"
      style="background-color: #FFFFFF; border-bottom: 1px solid #E0E0E0;"
    >
      <div class="flex items-center gap-2">
        <span class="text-xs font-semibold uppercase tracking-widest" style="color: #BB080B;">
          Мои воркспейсы
        </span>
        <span
          class="text-xs px-2 py-0.5 rounded-full font-bold"
          style="background-color: #BB080B; color: white;"
        >
          {{ workspaces.length }}
        </span>
      </div>

      <button
        @click="openModal"
        class="flex items-center gap-2 px-4 py-2 rounded text-sm font-semibold text-white transition-opacity hover:opacity-90"
        style="background-color: #BB080B;"
      >
        <span>+</span>
        <span>Новый воркспейс</span>
      </button>
    </div>

    <!-- Контент -->
    <div class="max-w-3xl mx-auto px-6 py-8">
      <div class="mb-6">
        <h1 class="text-2xl font-bold" style="color: #1A1A1A;">Workspaces</h1>
        <p class="text-sm mt-1" style="color: #6B6B6B;">
          Выберите воркспейс для работы
        </p>
      </div>

      <div class="flex flex-col gap-2">
        <div v-if="loading" class="text-sm" style="color: #6B6B6B;">Загрузка...</div>
        <div v-else-if="error" class="text-sm" style="color: #BB080B;">{{ error }}</div>
        <div v-else-if="workspaces.length === 0" class="text-sm" style="color: #6B6B6B;">
          Нет воркспейсов. Создайте первый!
        </div>
        <WorkspaceItem
          v-else
          v-for="workspace in workspaces"
          :key="workspace.id"
          :workspace="workspace"
        />
      </div>
    </div>

    <!-- Попап -->
    <Transition name="fade">
      <div
        v-if="showModal"
        class="fixed inset-0 z-50 flex items-center justify-center"
        style="background-color: rgba(0,0,0,0.4);"
        @click.self="closeModal"
      >
        <div
          class="w-full max-w-md rounded-lg p-6 shadow-xl"
          style="background-color: #FFFFFF;"
        >
          <!-- Шапка -->
          <div class="flex items-center justify-between mb-5">
            <h2 class="text-base font-bold" style="color: #1A1A1A;">
              Новый воркспейс
            </h2>
            <button
              @click="closeModal"
              class="text-lg leading-none hover:opacity-60 transition-opacity"
              style="color: #6B6B6B;"
            >
              ✕
            </button>
          </div>

          <!-- Поле ввода -->
          <label class="block text-xs font-semibold uppercase tracking-wider mb-1" style="color: #6B6B6B;">
            Название
          </label>
          <input
            v-model="newTitle"
            @keyup.enter="createWorkspace"
            type="text"
            placeholder="Например: Проект Alpha"
            class="w-full px-3 py-2 rounded border text-sm outline-none transition"
            style="border-color: #E0E0E0; color: #1A1A1A;"
            :style="createError ? 'border-color: #BB080B;' : ''"
            autofocus
          />
          <p v-if="createError" class="text-xs mt-1" style="color: #BB080B;">
            {{ createError }}
          </p>

          <!-- Кнопки -->
          <div class="flex justify-end gap-2 mt-5">
            <button
              @click="closeModal"
              class="px-4 py-2 rounded text-sm font-semibold transition-opacity hover:opacity-70"
              style="color: #6B6B6B; background-color: #F0F0F0;"
            >
              Отмена
            </button>
            <button
              @click="createWorkspace"
              :disabled="creating"
              class="px-4 py-2 rounded text-sm font-semibold text-white transition-opacity hover:opacity-90 disabled:opacity-50"
              style="background-color: #BB080B;"
            >
              {{ creating ? 'Создание...' : 'Создать' }}
            </button>
          </div>
        </div>
      </div>
    </Transition>

  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.15s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
