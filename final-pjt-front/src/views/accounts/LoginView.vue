<template>
  <div>
    <h1>로그인 페이지</h1>
    <form @submit.prevent="login">
      <label for="id">ID</label>
      <input type="text" id="id" v-model="username">
      <label for="pass">Password</label>
      <input type="password" id="pass" v-model="password">
      <input type="submit">
    </form>
  </div>
</template>


<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref('')
const password = ref('')

const login = function () {
  const payload = {
    username:username.value,
    password : password.value
  }
  store.LogIn(payload)
}
</script>

<style scoped>

</style>