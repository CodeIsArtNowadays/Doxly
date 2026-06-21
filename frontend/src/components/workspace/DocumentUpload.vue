<script setup>
import { ref } from 'vue'

const emit = defineEmits(['upload'])
const inputRef = ref(null)

function openPicker() {
  inputRef.value.click()
}

function onFileChange(e) {
  const file = e.target.files[0]
  if (!file) return
  emit('upload', file)
  // Сбрасываем input чтобы можно было загрузить тот же файл повторно
  e.target.value = ''
}
</script>

<template>
  <div>
    <input
      ref="inputRef"
      type="file"
      accept=".pdf,.txt,.docx"
      class="hidden"
      @change="onFileChange"
    />
    <button
      @click="openPicker"
      class="w-6 h-6 rounded flex items-center justify-center text-white text-sm font-bold transition-opacity hover:opacity-80"
      style="background-color: #BB080B;"
      title="Загрузить документ"
    >
      +
    </button>
  </div>
</template>
