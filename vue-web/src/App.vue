<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import NavigationBar from "@/components/NavigationBar.vue";
import HomeView from "@/views/HomeView.vue";
import Live2d from "@/components/Live-2d.vue";


</script>

<template>
  <body>
  <NavigationBar />
  <HomeView />
  <Live2d/>
  </body>

  <RouterView />
</template>

<style scoped>

</style>
