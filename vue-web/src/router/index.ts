import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

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
      component: () => import('@/views/AboutView.vue'),
    },
    {
      path: '/resume',
      name: 'resume',
      component: () => import('@/views/ResumeView.vue'),
    },
    {
      path: '/yuxin_user',
      name: 'yuxin_user',
      component: () => import('@/views/YuxinUserView.vue'),
    },
    {
      path: '/gateway',
      name: 'gateway',
      component: () => import('@/views/ChartView.vue'),
    },
  ],
})

export default router
