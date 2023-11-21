<script setup>
import axios from 'axios';
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from './stores/counter';

const store = useCounterStore()

</script>

<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <RouterLink class="navbar-brand" to="/home">Home</RouterLink>

      <div class="collapse navbar-collapse">
        <ul class="navbar-nav me-auto">
          <li class="nav-item" v-if="!store.isAuthenticated">
            <RouterLink class="nav-link" to="/login">LogIn</RouterLink>
          </li>
          <li class="nav-item" v-if="!store.isAuthenticated">
            <RouterLink class="nav-link" to="/signup">SignUp</RouterLink>
          </li>
          <li class="nav-item" v-if="store.isAuthenticated">
            <RouterLink class="nav-link" :to="{name:'profile',params:{username:store.tempUsername}}">프로필</RouterLink>
          </li>
        </ul>

        <button class="btn btn-outline-light" @click.prevent="store.logout()" v-if="store.isAuthenticated">로그아웃</button>
      </div>
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
