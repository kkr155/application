<template>
  <header class="status-bar">
    <div class="title">状态栏</div>
    <div class="actions">
      <button class="action-btn">刷新</button>
      <button class="action-btn">设置</button>
    </div>
  </header>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'StatusBar',
});
</script>

<style scoped>
.status-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 1rem;
  background-color: var(--primary-color);
  color: white;
  box-shadow: var(--shadow);
}

.title {
  font-size: 1.2rem;
  font-weight: bold;
}

.actions {
  display: flex;
  gap: 0.5rem;
}

.action-btn {
  background-color: var(--secondary-color);
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: var(--radius);
  cursor: pointer;
  transition: var(--transition);
}

.action-btn:hover {
  background-color: var(--color);
}
</style>
