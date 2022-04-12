import {createRouter, createWebHistory} from 'vue-router'
import Home from '@/pages/Home.vue'
import Portfolio from "@/pages/Portfolio";
import About from "@/pages/About";
import Services from "@/pages/Services";
import Reviews from "@/pages/Reviews";
import Profile from "@/pages/Profile";
import PageNotFound from "@/pages/PageNotFound";

const routes = [
    {
        path: '/',
        component: Home,
        meta: {transition: 'slide'}
    },
    {
        path: '/portfolio',
        component: Portfolio,
        meta: {transition: 'slide-left'}
    },
    {
        path: '/about',
        component: About,
    },
    {
        path: '/services',
        component: Services,
    },
    {
        path: '/reviews',
        component: Reviews,
    },
    {
        path: '/profile',
        component: Profile,
    },
    {
        path: "/:catchAll(.*)",
        component: PageNotFound
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
