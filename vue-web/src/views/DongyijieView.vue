<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'

const chars = ['傻', '逼'] // 可替换为任何两个中文字符
const fontSize = ref(100)

const updateFontSize = () => {
  // 取窗口宽高的最小值作为基准
  const minDimension = Math.min(window.innerWidth, window.innerHeight)
  fontSize.value = minDimension * 0.4 // 占据屏幕40%空间
}

onMounted(() => {
  updateFontSize()
  window.addEventListener('resize', updateFontSize)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateFontSize)
})
</script>

<template>
  <div class="text-container">
    <div
      v-for="(char, index) in chars"
      :key="index"
      class="char"
      :style="{ fontSize: `${fontSize}px` }"
    >
      {{ char }}
    </div>
  </div>
</template>

<style scoped>
.text-container {
  display: flex;
  height: 100vh; /* 视口高度 */
  width: 100vw;  /* 视口宽度 */
  overflow: hidden; /* 防止滚动条 */
}

.char {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: 900;
  text-align: center;
  transition: font-size 0.3s ease;
  will-change: transform; /* 优化动画性能 */
}
</style>
