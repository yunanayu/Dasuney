import { createRouter, createWebHistory } from 'vue-router'
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
      component: HomeView
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
      component: MovieDetailView
    },
    {
      path: '/profile/:username',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/actorlike/:username',
      name: 'actorlike',
      component: ActorLikeView
    },
    {
      path: '/directorlike/:username',
      name: 'directorlike',
      component: DirectorLikeView
    },
    {
      path: '/hopemovie',
      name: 'hopemovie',
      component: HopeMovieView
    },
    {
      path: '/starrating',
      name: 'starrating',
      component: StarRatingView
    },
  ]
})

export default router
