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
      <!-- <RouterLink :to="{name:'profile',params:{username:store.tempUsername}}" v-if="store.isAuthenticated">프로필 |</RouterLink>  -->
      <button @click.prevent="store.logout()" v-if="store.isAuthenticated">로그아웃</button>
    </nav>
  <RouterView />
  </div>
</template>

<style scoped>
#app {
  background-color: #0b1035;
  font-family: 'Arial', sans-serif;
  color: white;
  
  
}
</style>
