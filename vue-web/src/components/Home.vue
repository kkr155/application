<template>
  <div class="home">
    <main class="content">
      <h1>欢迎来到我的网站</h1>
      <p>这是一个包含状态栏和页面内容的示例。</p>
    </main>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue";

export default defineComponent({
  name: 'Home',
});
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.content {
  flex: 1;
  padding: 2rem;
  background-color: var(--light-bg);
  color: var(--color);
  overflow-y: auto;
}

h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

p {
  font-size: 1rem;
  line-height: 1.6;
}
</style>
