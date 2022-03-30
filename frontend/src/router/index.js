import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/pages/HomeView.vue'
import PortfolioView from "@/pages/PortfolioView";

const routes = [
  {
    path: '/',
    component: HomeView,
    meta: { transition: 'slide' }
  },
  {
    path: '/portfolio',
    component: PortfolioView,
    meta: { transition: 'slide-left' }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
