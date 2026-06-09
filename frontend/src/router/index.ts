import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/timeline' },
    {
      path: '/timeline',
      name: 'Timeline',
      component: () => import('@/pages/TimelinePage.vue'),
    },
    {
      path: '/map',
      name: 'Map',
      component: () => import('@/pages/MapPage.vue'),
    },
    {
      path: '/event/:id',
      name: 'EventDetail',
      component: () => import('@/pages/EventDetailPage.vue'),
    },
  ],
})

export default router
