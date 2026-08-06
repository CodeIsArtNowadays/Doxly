<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import DocumentUpload from './DocumentUpload.vue'
import api from '@/api/axios'

const props = defineProps({
  members: Array,
  documents: Array,
})

const emit = defineEmits(['upload', 'memberAdded'])

const route = useRoute()
const workspaceId = route.params.id

// --- Modal state ---
const showModal = ref(false)
const adding = ref(false)
const addError = ref(null)
const form = ref({ username: '', role: 'member' })

function openModal() {
  form.value = { username: '', role: 'member' }
  addError.value = null
  showModal.value = true
}

function closeModal() {
  showModal.value = false
}

async function addMember() {
  if (!form.value.username.trim()) {
    addError.value = 'Введите имя пользователя'
    return
  }

  adding.value = true
  addError.value = null

  try {
    await api.patch(`/${workspaceId}/members`, {
      username: form.value.username.trim(),
      role: form.value.role
    })
    emit('memberAdded')
    closeModal()
  } catch (e) {
    addError.value = e.response?.data?.detail ?? 'Не удалось добавить участника'
  } finally {
    adding.value = false
  }
}
</script>

<template>
  <aside
    class="w-64 flex flex-col overflow-hidden flex-shrink-0"
    style="background: #FFFFFF; border-right: 1px solid #E0E0E0;"
  >

    <!-- Участники -->
    <div class="flex flex-col flex-1 overflow-y-auto">
      <div
        class="px-4 py-3 flex items-center justify-between"
        style="border-bottom: 1px solid #E0E0E0;"
      >
        <div class="flex items-center gap-2">
          <span class="text-xs font-bold uppercase tracking-widest" style="color: #BB080B;">
            Участники
          </span>
          <span
            class="text-xs px-1.5 py-0.5 rounded-full font-bold"
            style="background-color: #BB080B; color: white;"
          >
            {{ members.length }}
          </span>
        </div>

        <!-- Кнопка добавить участника -->
        <button
          @click="openModal"
          class="w-6 h-6 flex items-center justify-center rounded-full transition-colors hover:bg-red-50"
          style="color: #BB080B;"
          title="Добавить участника"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
          </svg>
        </button>
      </div>

      <div class="flex flex-col gap-1 p-3">
        <div
          v-for="member in members"
          :key="member.id"
          class="flex items-center gap-2.5 px-2 py-2 rounded transition-colors hover:bg-gray-50"
        >
          <div
            class="w-7 h-7 rounded-full flex items-center justify-center text-white text-xs font-bold flex-shrink-0"
            style="background-color: #BB080B;"
          >
            {{ member.username.charAt(0).toUpperCase() }}
          </div>
          <div class="flex flex-col min-w-0">
            <span class="text-sm font-medium truncate" style="color: #1A1A1A;">
              {{ member.username }}
            </span>
            <span class="text-xs truncate" style="color: #AAAAAA;">
              {{ member.role === 'admin' ? 'Админ' : 'Участник' }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Документы -->
    <div
      class="flex flex-col"
      style="border-top: 1px solid #E0E0E0;"
    >
      <div
        class="px-4 py-3 flex items-center justify-between"
        style="border-bottom: 1px solid #E0E0E0;"
      >
        <div class="flex items-center gap-2">
          <span class="text-xs font-bold uppercase tracking-widest" style="color: #BB080B;">
            Документы
          </span>
          <span
            class="text-xs px-1.5 py-0.5 rounded-full font-bold"
            style="background-color: #BB080B; color: white;"
          >
            {{ documents.length }}
          </span>
        </div>
        <DocumentUpload @upload="emit('upload', $event)" />
      </div>

      <div class="flex flex-col gap-1 p-3 max-h-48 overflow-y-auto">
        <div
          v-if="documents.length === 0"
          class="text-xs text-center py-4"
          style="color: #AAAAAA;"
        >
          Нет документов
        </div>

        <div
          v-for="doc in documents"
          :key="doc.id"
          class="flex items-center gap-2.5 px-2 py-2 rounded transition-colors hover:bg-gray-50"
        >
          <div
            class="w-7 h-7 rounded flex items-center justify-center text-white text-xs font-bold flex-shrink-0"
            style="background-color: #9A0002;"
          >
            {{ doc.title.split('.').pop().toUpperCase().slice(0, 3) }}
          </div>
          <span class="text-xs truncate" style="color: #1A1A1A;">{{ doc.title }}</span>
        </div>
      </div>
    </div>

    <!-- Modal Overlay -->
    <Transition name="fade">
      <div
        v-if="showModal"
        class="fixed inset-0 z-50 flex items-center justify-center px-4"
        style="background: rgba(0,0,0,0.45);"
        @click.self="closeModal"
      >
        <Transition name="slide-up">
          <div
            v-if="showModal"
            class="w-full max-w-sm rounded-2xl p-6 shadow-2xl"
            style="background: #FFFFFF;"
          >
            <!-- Header -->
            <div class="flex items-center justify-between mb-5">
              <h2 class="text-base font-bold" style="color: #1A1A1A;">Добавить участника</h2>
              <button
                @click="closeModal"
                class="w-7 h-7 flex items-center justify-center rounded-full transition-colors hover:bg-gray-100"
                style="color: #6B6B6B;"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>

            <div class="flex flex-col gap-4">

              <!-- Username -->
              <div class="flex flex-col gap-1.5">
                <label class="text-xs font-semibold uppercase tracking-widest" style="color: #BB080B;">
                  Имя пользователя
                </label>
                <input
                  v-model="form.username"
                  type="text"
                  placeholder="username"
                  class="w-full px-3 py-2.5 rounded-xl text-sm outline-none transition-all"
                  style="border: 1.5px solid #E0E0E0; color: #1A1A1A;"
                  @keydown.enter="addMember"
                  @focus="e => e.target.style.borderColor = '#BB080B'"
                  @blur="e => e.target.style.borderColor = '#E0E0E0'"
                />
              </div>

              <!-- Role -->
              <div class="flex flex-col gap-1.5">
                <label class="text-xs font-semibold uppercase tracking-widest" style="color: #6B6B6B;">
                  Роль
                </label>
                <div class="flex gap-2">
                  <button
                    v-for="option in ['member', 'admin']"
                    :key="option"
                    @click="form.role = option"
                    class="flex-1 py-2 rounded-xl text-sm font-semibold transition-all"
                    :style="form.role === option
                      ? 'background-color: #BB080B; color: white; border: 1.5px solid #BB080B;'
                      : 'background-color: white; color: #6B6B6B; border: 1.5px solid #E0E0E0;'"
                  >
                    {{ option === 'member' ? 'Участник' : 'Админ' }}
                  </button>
                </div>
              </div>

              <!-- Error -->
              <p v-if="addError" class="text-xs" style="color: #BB080B;">
                {{ addError }}
              </p>

              <!-- Actions -->
              <div class="flex gap-3 pt-1">
                <button
                  @click="closeModal"
                  class="flex-1 py-2.5 rounded-xl text-sm font-semibold transition-colors hover:bg-gray-100"
                  style="color: #6B6B6B; border: 1.5px solid #E0E0E0;"
                >
                  Отмена
                </button>
                <button
                  @click="addMember"
                  :disabled="adding"
                  class="flex-1 py-2.5 rounded-xl text-sm font-semibold text-white transition-opacity"
                  :class="adding ? 'opacity-60 cursor-not-allowed' : 'hover:opacity-90'"
                  style="background-color: #BB080B;"
                >
                  <span v-if="adding" class="flex items-center justify-center gap-2">
                    <svg class="w-4 h-4 animate-spin" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
                      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"/>
                    </svg>
                    Добавляем...
                  </span>
                  <span v-else>Добавить</span>
                </button>
              </div>

            </div>
          </div>
        </Transition>
      </div>
    </Transition>

  </aside>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active { transition: opacity 0.2s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

.slide-up-enter-active, .slide-up-leave-active { transition: transform 0.2s ease, opacity 0.2s ease; }
.slide-up-enter-from, .slide-up-leave-to { transform: translateY(16px); opacity: 0; }
</style>

