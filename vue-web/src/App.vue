<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Home from "@/components/Home.vue";
import StatusBar from '@/components/Header.vue';


</script>

<template>
  <header>


<!--    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />-->

<!--    <div class="wrapper">-->
<!--      <HelloWorld msg="You did it!" />-->

<!--      <nav>-->
<!--        <RouterLink to="/">Home</RouterLink>-->
<!--        <RouterLink to="/about">About</RouterLink>-->
<!--      </nav>-->
<!--    </div>-->
  </header>
  <body>
  <StatusBar />
  <Home />-->
  </body>

  <RouterView />
</template>

<style scoped>

</style>
