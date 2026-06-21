<script setup>
import DocumentUpload from './DocumentUpload.vue'

// eslint-disable-next-line no-unused-vars
const props = defineProps({
  members: Array,
  documents: Array,
})

const emit = defineEmits(['upload'])
</script>

<template>
  <aside
    class="w-64 flex flex-col overflow-hidden flex-shrink-0"
    style="background: #FFFFFF; border-right: 1px solid #E0E0E0;"
  >

    <!-- Участники -->
    <div class="flex flex-col flex-1 overflow-y-auto">
      <div
        class="px-4 py-3 flex items-center gap-2"
        style="border-bottom: 1px solid #E0E0E0;"
      >
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
          <span class="text-sm font-medium truncate" style="color: #1A1A1A;">
            {{ member.username }}
          </span>
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
          <!-- Иконка по типу файла -->
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

  </aside>
</template>
