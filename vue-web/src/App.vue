<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavigationBar from "@/components/NavigationBar.vue";
import CopyRight from "@/components/CopyRight.vue";

</script>
<template>
  <body>
  <NavigationBar />
<!--  <Live2d/>-->
  <RouterView/>
  <CopyRight/>
  </body>

</template>

<style scoped>

</style>
