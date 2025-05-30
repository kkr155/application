import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ResumeView from '../views/ResumeView.vue'
import HotfixView from "@/views/HotfixView.vue";
import ChartView from "@/views/ChartView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
    },
    {
      path: '/resume',
      name: 'resume',
      component: ResumeView,
    },
    {
      path: '/hotfix',
      name: 'hotfix',
      component: HotfixView,
    },
    {
      path: '/gateway',
      name: 'gateway',
      component:  ChartView,
    },
  ],
})

export default router
