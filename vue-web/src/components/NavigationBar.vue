<script setup lang="ts">

import {ref,onMounted} from "vue";
// 主题状态
const theme = ref<'light' | 'dark'>('light')

onMounted(() => {
  const savedTheme = localStorage.getItem('resume-theme') as 'light' | 'dark' || 'light'
  theme.value = savedTheme
  document.documentElement.setAttribute('data-theme', theme.value)
})

// 主题切换功能
function toggleTheme() {
  const html = document.documentElement;
  const currentTheme = html.getAttribute('data-theme');
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  html.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
}
</script>

<template>
  <nav class="navbar">
<!--    <a href="/" class="nav-logo"></a>-->
    <a href="/" class="nav-logo">
      <span class="logo-text" data-text="kokoro">kokoro</span>
    </a>
    <ul class="nav-menu">
<!--      <li class="nav-item"><a href="/resume" class="nav-link">关于</a></li>-->
      <li class="nav-item">
        <button class="theme-toggle" @click="toggleTheme()">
          <span class="theme-icon">🌓</span>
        </button>
      </li>
    </ul>
  </nav>
</template>

<style scoped>
/* 导航栏基础样式 */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 5%;
  height: 60px; /* 固定高度 */
  background: var(--dark-bg);
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* 导航菜单 */
.nav-menu {
  display: flex;
  gap: 2rem;
  list-style: none;
  margin: 0;
  padding: 0;
  height: 100%; /* 继承navbar高度 */
}

/*左上文字*/
.logo-text {
  color: var(--dark);
  font-family: 'Courier New', monospace;
  font-weight: 700;
  position: relative;
}
/*悬停时*/
.logo-text::after {
  content: attr(data-text);
  position: absolute;
  left: 0;
  color: var(--secondary);
  width: 0;
  overflow: hidden;
  transition: width 0.5s ease;
}
.nav-logo:hover .logo-text::after {
  width: 100%;
}

/* 导航项（确保垂直居中） */
.nav-item {
  display: flex;
  align-items: center;
  height: 100%;
  position: relative;
}

.nav-logo {
  text-decoration: none;
  display: inline-flex;
}

/* 导航链接 */
.nav-link {
  color: rgba(255, 255, 255, 0.9);
  text-decoration: none;
  padding: 0.5rem 0;
  display: flex;
  align-items: center;
  height: 100%;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: var(--primary-color);
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--primary-color);
  transition: width 0.3s ease;
}

.nav-link:hover::after {
  width: 100%;
}

/* 主题切换按钮（精致版） */
.theme-toggle {
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: all 0.3s ease;
}


.theme-toggle:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: scale(1.1);
}

.theme-icon {
  font-size: 1.2rem;
  transition: transform 0.3s ease;
}

.theme-toggle:hover .theme-icon {
  transform: rotate(30deg);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .nav-menu {
    gap: 1rem;
  }

  .nav-link {
    font-size: 0.9rem;
  }

  .theme-toggle {
    width: 36px;
    height: 36px;
  }
}
</style>
