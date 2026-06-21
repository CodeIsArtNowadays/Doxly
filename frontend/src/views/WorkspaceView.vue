<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import api from '@/api/axios'
import WorkspaceSidebar from '@/components/workspace/WorkspaceSidebar.vue'
import WorkspaceChat from '@/components/workspace/WorkspaceChat.vue'

const route = useRoute()
const auth = useAuthStore()
const id = route.params.id

// --- State ---
const workspace = ref(null)
const members = ref([])
const messages = ref([])
const documents = ref([])
const loading = ref(true)
const ws = ref(null)

// --- WebSocket ---
function connectWS() {
  ws.value = new WebSocket(`ws://localhost:8000/${id}/channel`)

  ws.value.onopen = () => {
    ws.value.send(JSON.stringify({
      type: 'auth',
      content: { token: auth.token }
    }))
  }

  ws.value.onmessage = (event) => {
    console.log('WS raw:', event.data)
    const msg = JSON.parse(event.data)
    messages.value.push(msg)
  }


  ws.value.onerror = (e) => console.error('WS error', e)
  ws.value.onclose = () => console.log('WS closed')
}

function sendMessage(text) {
  if (!ws.value || ws.value.readyState !== WebSocket.OPEN) return
  ws.value.send(JSON.stringify({
    type: 'message',
    content: { message: text }
  }))
}

// --- API ---
async function fetchWorkspace() {
  const { data } = await api.get(`/${id}`)
  workspace.value = data.title
  members.value = data.members ?? []
}

async function fetchMessages() {
  const { data } = await api.get(`/${id}/channel`)
  messages.value = data ?? []
}

async function fetchDocuments() {
  const { data } = await api.get(`/${id}/documents`)
  documents.value = data ?? []
}

async function handleUpload(file) {
  const formData = new FormData()
  formData.append('file', file)
  await api.post(`/${id}/upload`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })
  // Даём таске время отработать, потом обновляем список
  setTimeout(async () => {
    await fetchDocuments()
  }, 2000)
}


// --- Lifecycle ---
onMounted(async () => {
  await Promise.all([fetchWorkspace(), fetchMessages(), fetchDocuments()])
  loading.value = false
  connectWS()
})

onUnmounted(() => {
  ws.value?.close()
})
</script>

<template>
<div class="flex flex-col overflow-hidden" style="height: 100%; background-color: #F5F5F5;">


    <!-- Лоадер -->
    <div v-if="loading" class="flex-1 flex items-center justify-center">
      <div class="flex flex-col items-center gap-3">
        <div
          class="w-10 h-10 rounded-sm flex items-center justify-center text-white text-sm font-black animate-pulse"
          style="background-color: #BB080B;"
        >
          WS
        </div>
        <span class="text-sm" style="color: #6B6B6B;">Загружаем воркспейс...</span>
      </div>
    </div>

    <!-- Контент -->
    <template v-else>

      <!-- Заголовок -->
      <div
        class="w-full px-6 py-3 flex items-center gap-3 flex-shrink-0"
        style="background: #FFFFFF; border-bottom: 1px solid #E0E0E0;"
      >
        <h1 class="text-base font-bold" style="color: #1A1A1A;">{{ workspace }}</h1>
      </div>

      <!-- Основной layout -->
      <div class="flex flex-1 min-h-0">

        <WorkspaceSidebar
          :members="members"
          :documents="documents"
          @upload="handleUpload"
        />

        <WorkspaceChat
          :messages="messages"
          @send="sendMessage"
        />

      </div>

    </template>
  </div>
</template>
