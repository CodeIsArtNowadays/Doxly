<template>
  <div
    @click="open"
    @mouseenter="hovered = true"
    @mouseleave="hovered = false"
    class="cursor-pointer rounded px-6 py-4 w-full flex items-center justify-between transition-all duration-150"
    :style="{
      background: hovered ? '#FFF5F5' : '#FFFFFF',
      border: '1.5px solid ' + (hovered ? '#BB080B' : '#E0E0E0'),
      boxShadow: hovered ? '0 2px 12px rgba(187,8,11,0.10)' : '0 1px 3px rgba(0,0,0,0.06)'
    }"
  >
    <!-- Левая часть -->
    <div class="flex items-center gap-4">
      <div
        class="w-8 h-8 rounded flex items-center justify-center text-xs font-bold transition-colors"
        :style="{
          background: hovered ? '#BB080B' : '#F5F5F5',
          color: hovered ? '#FFFFFF' : '#9A0002'
        }"
      >
        {{ workspace.id }}
      </div>

      <div class="flex flex-col">
        <span class="text-base font-semibold" style="color: #1A1A1A;">
          {{ workspace.name }}
        </span>
        <span class="text-xs" style="color: #6B6B6B;">
          Workspace · ID {{ workspace.id }}
        </span>
      </div>
    </div>

    <!-- Стрелка -->
    <div
      class="flex items-center gap-1 text-sm font-semibold transition-all"
      :style="{ color: hovered ? '#BB080B' : '#AAAAAA' }"
    >
      <span>Открыть</span>
      <span class="text-base">→</span>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  workspace: Object
})

const router = useRouter()
const hovered = ref(false)

function open() {
  router.push(`/workspace/${props.workspace.id}`)
}
</script>
