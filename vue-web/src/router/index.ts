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
      path: '/resume',
      name: 'resume',
      component: () => import('@/views/ResumeView.vue'),
    },
    {
      path: '/yuxin-user',
      name: 'yuxin-user',
      component: () => import('@/views/YuxinUserView.vue'),
    },
    {
      path: '/pgyer-manage',
      name: 'pgyer-manage',
      component: () => import('@/views/PgyerManageView.vue'),
    },
    {
      path: '/dongyijie',
      name: 'dongyijie',
      component: () => import('@/views/DongyijieView.vue'),
    }

  ],
})

export default router
