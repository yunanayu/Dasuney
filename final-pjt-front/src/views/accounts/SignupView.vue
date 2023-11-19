<template>
  <div>
    <h1>회원가입 페이지</h1>
    <form @submit.prevent="signup">
      <label for="id">ID</label>
      <input type="text" id="id" v-model="username">
      <label for="pass1">Password1</label>
      <input type="password" id="pass1" v-model="password1">
      <label for="pass2">Password2</label>
      <input type="password" id="pass2" v-model="password2">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const username = ref('')
const password1 = ref('')
const password2 = ref('')

const signup = function () {
  const payload = {
    username : username.value,
    password1 : password1.value,
    password2 : password2.value
  }
  store.SignUp(payload)
}
</script>

<style scoped>

</style>