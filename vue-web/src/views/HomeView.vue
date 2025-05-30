<script setup lang="ts">
import { ref } from 'vue'

// 功能模块配置（避免硬编码）
const modules = [
  {
    id: 'lab',
    title: '简历',
    icon: 'flask',
    path: 'resume',
    glowColor: '#2BD2FF'
  },
  {
    id: 'hotfix',
    title: '热加载',
    icon: 'database',
    path: '/hotfix',
    glowColor: '#6B5AED'
  },
  {
    id: 'gateway',
    title: '饼图预览',
    icon: 'portal',
    path: 'gateway',
    glowColor: '#FF4D4D'
  }
]

</script>

<template>
  <div class="quantum-container">
    <!-- 动态星轨背景层 -->
    <div class="stellar-background">
      <div class="quantum-tunnel"></div>
    </div>

    <!-- 功能矩阵层 -->
    <nav class="hologram-matrix">
      <router-link
        v-for="module in modules"
        :key="module.id"
        :to="module.path"
        class="quantum-card"
        :style="{ '--glow-color': module.glowColor }"
      >
        <div class="icon-wrapper">
          <font-awesome-icon
            :icon="`fa-solid fa-${module.icon}`"
            class="portal-icon"
          />
        </div>
        <div class="data-stream"></div>
        <h3>{{ module.title }}</h3>
      </router-link>
    </nav>


  </div>
</template>

<style scoped>
/* 动态量子隧道背景 */
.quantum-tunnel {
  position: fixed;
  width: 150vw;
  height: 150vh;
  background:
    linear-gradient(
      45deg,
      rgba(43,210,255,0.05) 0%,
      rgba(107,90,237,0.05) 50%,
      rgba(255,77,77,0.05) 100%
    );
  animation: tunnel-flow 30s linear infinite;
}

.hologram-matrix {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 4rem;
  padding: 8rem;
  position: relative;
  z-index: 2;
}

.quantum-card {
  position: relative;
  height: 200px;
  align-content: center;
  text-align: center;
  background: rgba(26,26,46,0.7);
  border: 1px solid var(--accent);
  border-radius: 16px;
  transition: all 0.5s cubic-bezier(0.68, -0.55, 0.27, 1.55);
  overflow: hidden;
}

.quantum-card:hover {
  transform: translateY(-10px) rotateX(5deg);
  box-shadow: 0 0 40px var(--accent);
}

.portal-icon {
  font-size: 4rem;
  color: var(--accent);
  filter: drop-shadow(0 0 8px var(--accent));
  transition: transform 0.3s ease;
}

.data-stream {
  position: absolute;
  bottom: 0;
  height: 4px;
  width: 100%;
  background: linear-gradient(90deg,
  transparent 0%,
  var(--accent) 50%,
  transparent 100%
  );
  animation: data-flow 2s linear infinite;
}

@keyframes tunnel-flow {
  from { transform: rotate(0deg) translateX(-50%); }
  to { transform: rotate(360deg) translateX(-50%); }
}

@keyframes data-flow {
  from { background-position: -200% 0; }
  to { background-position: 200% 0; }
}
</style>
