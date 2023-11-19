<script setup>
import axios from 'axios';
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from './stores/counter';

const store = useCounterStore()



</script>

<template>
      <nav>
        <RouterLink to="/">Home</RouterLink> |
        <RouterLink to="/login">Login</RouterLink> |
        <RouterLink to="/signup">SignUp</RouterLink> |
        <button @click.prevent="store.logout()">LogOut</button>
      </nav>
  <RouterView />
</template>

<style scoped>
</style>
