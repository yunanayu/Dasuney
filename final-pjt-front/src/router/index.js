import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '../stores/counter'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ActorLikeView from '@/views/Profiles/ActorLikeView.vue'
import DirectorLikeView from '@/views/Profiles/DirectorLikeView.vue'
import HopeMovieView from '@/views/Profiles/HopeMovieView.vue'
import StarRatingView from '@/views/Profiles/StarRatingView.vue'
import IntroView from '@/views/accounts/IntroView.vue'
import AniView from '@/views/accounts/AniView.vue'
import ActorMovieView from '@/views/ActorMovieView.vue'
import DirectorMovieView from '@/views/DirectorMovieView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'first',
      component: AniView
    },
    {
      path: '/intro',
      name: 'intro',
      component: IntroView
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView,
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/moviedetail/:movieId',
      name: 'moviedetail',
      component: MovieDetailView,
      meta: { requiresAuth: true }
    },
    {
      path: '/profile/:username',
      name: 'profile',
      component: ProfileView,
      meta: { requiresAuth: true }
    },
    {
      path: '/actorlike/:username',
      name: 'actorlike',
      component: ActorLikeView,
      meta: { requiresAuth: true }
    },
    {
      path: '/directorlike/:username',
      name: 'directorlike',
      component: DirectorLikeView,
      meta: { requiresAuth: true }
    },
    {
      path: '/hopemovie/:username',
      name: 'hopemovie',
      component: HopeMovieView,
      meta: { requiresAuth: true }
    },
    {
      path: '/starrating/:username',
      name: 'starrating',
      component: StarRatingView,
      meta: { requiresAuth: true }
    },
    {
      path: '/actormovielist/:actorid',
      name: 'actormovielist',
      component: ActorMovieView,
      meta: { requiresAuth: true }
    },
    {
      path: '/directormovielist/:directorid',
      name: 'directormovielist',
      component: DirectorMovieView,
      meta: { requiresAuth: true }
    },
  ]
})

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if ( to.meta.requiresAuth && !store.isAuthenticated) {
    window.alert('로그인이 필요합니다.')
    return {name:'intro'}
  }
  if ((to.name === 'signup' || to.name === 'login') && (store.isAuthenticated)) {
    window.alert('이미 로그인이 되어있습니다.')
    return {name:'home'}
  }
})

export default router
