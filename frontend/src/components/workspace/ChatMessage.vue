<script setup>
import { useAuthStore } from '@/stores/auth'

const props = defineProps({
  message: Object
})

const auth = useAuthStore()
const isOwn = props.message.username === auth.username
</script>

<template>
  <div
    class="flex gap-2.5"
    :class="isOwn ? 'flex-row-reverse' : 'flex-row'"
  >
    <!-- Аватар -->
    

    <!-- Пузырь -->
    <div class="flex flex-col gap-1 max-w-xs" :class="isOwn ? 'items-end' : 'items-start'">
      <span class="text-xs font-semibold" style="color: #6B6B6B;">
        {{ message.author?.username }}
      </span>
      <div
        class="px-4 py-2.5 rounded-lg text-sm leading-relaxed"
        :style="isOwn
          ? 'background-color: #BB080B; color: #FFFFFF;'
          : 'background-color: #FFFFFF; color: #1A1A1A; border: 1px solid #E0E0E0;'"
      >
        {{ message.text }}
      </div>
    </div>
  </div>
</template>
