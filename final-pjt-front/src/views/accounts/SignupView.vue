<template>
  <div>
    <h1 class="logo">Sign Up</h1>
    <form @submit.prevent="signup" class="card">
      <label for="id">ID</label>
      <input type="text" id="id" v-model="username" class="login">
      <label for="pass1">Password</label>
      <input type="password" id="pass1" v-model="password1" class="login">
      <label for="pass2">Password Confirm</label>
      <input type="password" id="pass2" v-model="password2" class="login">
      <input type="submit" value="회원가입" class="btn btn-primary btn-block" style="margin-top: 30px;">
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
.logo {
  text-align: center;
  font-family: disney;
  font-size: 80px;
  margin-bottom: 30px;
}
.card {
  width: 400px;
  height: 400px;
  text-align: center;
  margin: 0 auto;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  
}
label {
  font-size: 30px;
  text-align: left;
}
.login {
  height: 40px;
  border: 0px;
  border-radius: 8px;
  border-bottom: 1px solid;
  border-color: darkcyan;
  background-color: aliceblue;
}

</style>