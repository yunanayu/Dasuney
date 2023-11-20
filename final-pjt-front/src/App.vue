<script setup>
import axios from 'axios';
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from './stores/counter';

const store = useCounterStore()

</script>

<template>
  <div id="app">
    <nav>
      <RouterLink to="/">Home</RouterLink> |
      <RouterLink to="/login" v-if="!store.isAuthenticated">LogIn |</RouterLink>
      <RouterLink to="/signup" v-if="!store.isAuthenticated"> SignUp</RouterLink>
      <RouterLink to="/profile" v-if="store.isAuthenticated">프로필 |</RouterLink> 
      <button @click.prevent="store.logout()" v-if="store.isAuthenticated">로그아웃</button>
    </nav>
  <RouterView />
  </div>
</template>

<style scoped>
#app {
  /* background-image: url('@/assets/wallpaperbetter.jpg'); */
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;

  /* 나머지 스타일 설정 */
  font-family: 'Arial', sans-serif;
  color: #ffffff;
  width: 100%
  
}
</style>
