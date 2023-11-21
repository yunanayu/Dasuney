<script setup>
import axios from 'axios';
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from './stores/counter';

const store = useCounterStore()

</script>

<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark navtext">
      <RouterLink class="navbar-brand" to="/home" style="font-size: 40px;" v-show="store.isAuthenticated">Dasuney+</RouterLink>
      <RouterLink class="navbar-brand" to="/intro" style="font-size: 40px;"  v-show="!store.isAuthenticated">Dasuney+</RouterLink>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav me-auto">
          <li class="nav-item" v-if="store.isAuthenticated">
            <RouterLink class="nav-link" :to="{name:'profile',params:{username:store.tempUsername}}">Profile</RouterLink>
          </li>
        </ul>
        <button class="btn btn-outline-light" @click.prevent="store.logout()" v-if="store.isAuthenticated" style="font-size: 35px;">LogOut</button>
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
.navtext {
  font-family: disney;
  font-size: 30px;
}
.navbar-brand {
  margin-left: 15px;
}
.btn-outline-light {
  margin-right: 20px;
}
</style>
