<script setup lang="ts">
// 主题切换功能
// 主题切换
function toggleTheme() {
  const html = document.documentElement;
  const currentTheme = html.getAttribute('data-theme');
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  html.setAttribute('data-theme', newTheme);
  // 保存用户偏好
  localStorage.setItem('theme', newTheme);
}

</script>

<template>
  <nav class="navbar">
    <a href="/" class="nav-logo">kkr</a>
    <ul class="nav-menu">
      <li><a href="/distribute" class="nav-link">APK管理</a></li>
      <li><a href="/projects" class="nav-link">Api测试</a></li>
      <li><a href="/resume" class="nav-link">关于</a></li>
      <li><button class="theme-toggle" @click="toggleTheme()">🌓</button></li>
    </ul>
  </nav>
</template>



<style scoped>
/* 导航栏 */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 5%;
  background: var(--dark-bg);
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.nav-logo {
  font-size: 1.5rem;
  color: white;
  font-weight: 700;
  text-decoration: none;
  transition: var(--transition);
}

.nav-menu {
  display: flex;
  gap: 2rem;
  list-style: none;
}

.nav-link {
  color: rgba(255, 255, 255, 0.9);
  text-decoration: none;
  position: relative;
  padding: 0.5rem 0;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--primary-color);
  transition: var(--transition);
}

.nav-link:hover::after {
  width: 100%;
}

@media (max-width: 768px) {
  .nav-menu {
    display: none;
  }
}

/* 主题切换按钮 */
.theme-toggle {
  position: fixed;
  top: 1rem;
  right: 1rem;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--primary-color);
  border: none;
  cursor: pointer;
  box-shadow: var(--shadow);
}
</style>
