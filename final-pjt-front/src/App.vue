<script setup>
import axios from 'axios';
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from './stores/counter';

const store = useCounterStore()

</script>

<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark navtext">
      <div >
        <RouterLink class="navbar-brand" to="/home" style="font-size: 40px;" v-show="store.isAuthenticated">Dasuney+</RouterLink>
        <RouterLink class="navbar-brand" to="/intro" style="font-size: 40px;" v-show="!store.isAuthenticated">Dasuney+</RouterLink>
      </div>
      <div class="nav-item me-auto" v-if="store.isAuthenticated">
        <RouterLink class="nav-link" :to="{name:'profile',params:{username:store.tempUsername}}">Profile</RouterLink>
      </div>
      <div class="collapse navbar-collapse" id="navbarNav"></div>
      <!-- 로그아웃 버튼은 화면이 작아졌을 때도 보이게 설정 -->
      <button class="btn btn-outline-light" @click.prevent="store.logout()" v-if="store.isAuthenticated" style="font-size: 35px;">LogOut</button>
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
.nav-link {
  text-align: left;
}

</style>
