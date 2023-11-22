<template>
  <div>
    <h1 class="logo">Login</h1>
    <form @submit.prevent="login" class="card">
      <label for="id">ID</label>
      <input type="text" id="id" v-model="username" class="login">
      <label for="pass">Password</label>
      <input type="password" id="pass" v-model="password" class="login">
      <input type="submit" value="로그인" class="btn btn-primary btn-block" style="margin-top: 30px;">
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
.logo {
  text-align: center;
  font-family: disney;
  font-size: 80px;
  margin-bottom: 30px;
}
.card {
  width: 400px;
  height: 300px;
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