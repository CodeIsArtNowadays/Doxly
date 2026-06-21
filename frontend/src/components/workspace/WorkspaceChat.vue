<script setup>
import { ref, nextTick, watch } from 'vue'
import ChatMessage from './ChatMessage.vue'

const props = defineProps({
  messages: Array,
})

const emit = defineEmits(['send'])

const text = ref('')
const scrollRef = ref(null)

function handleSend() {
  const trimmed = text.value.trim()
  if (!trimmed) return
  emit('send', trimmed)
  text.value = ''
}

function handleKeydown(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault()
    handleSend()
  }
}

// Автоскролл вниз при новых сообщениях
watch(() => props.messages.length, async () => {
  await nextTick()
  if (scrollRef.value) {
    scrollRef.value.scrollTop = scrollRef.value.scrollHeight
  }
})
</script>

<template>
  
  <div class="flex flex-col flex-1 min-h-0 overflow-hidden">


    <!-- Сообщения -->
    <div
      ref="scrollRef"
      class="flex-1 overflow-y-auto px-6 py-4 flex flex-col gap-4"
      style="background-color: #F5F5F5;"
    >
      <div
        v-if="messages.length === 0"
        class="flex-1 flex items-center justify-center h-full"
      >
        <div class="flex flex-col items-center gap-2 opacity-40">
          <div
            class="w-10 h-10 rounded-sm flex items-center justify-center text-white text-sm font-black"
            style="background-color: #BB080B;"
          >
            #
          </div>
          <span class="text-sm" style="color: #6B6B6B;">Сообщений пока нет</span>
        </div>
      </div>

      <ChatMessage
        v-for="(msg, index) in messages"
        :key="index"
        :message="msg"
      />
    </div>

    <!-- Строка ввода -->
    <div
      class="px-4 py-3 flex items-end gap-3 flex-shrink-0"
      style="background: #FFFFFF; border-top: 1px solid #E0E0E0;"
    >
      <textarea
        v-model="text"
        @keydown="handleKeydown"
        placeholder="Написать сообщение... (Enter — отправить, Shift+Enter — новая строка)"
        rows="1"
        class="flex-1 px-4 py-2.5 rounded text-sm outline-none resize-none"
        style="
          border: 1.5px solid #E0E0E0;
          color: #1A1A1A;
          background: #FAFAFA;
          max-height: 120px;
        "
        @focus="$event.target.style.borderColor = '#BB080B'"
        @blur="$event.target.style.borderColor = '#E0E0E0'"
        @input="$event.target.style.height = 'auto'; $event.target.style.height = $event.target.scrollHeight + 'px'"
      />

      <button
        @click="handleSend"
        class="px-4 py-2.5 rounded text-sm font-semibold text-white transition-opacity hover:opacity-90 flex-shrink-0"
        style="background-color: #BB080B;"
      >
        →
      </button>
    </div>

  </div>
</template>
