<template>
  <div>
    <h1>갬동님 상세정보 페이지 입니당....</h1>
    <img :src="(`https://image.tmdb.org/t/p/w500/${directorInfo.profile_path}`)" alt="">
    <p> 이름 : {{ directorInfo.name }}</p>
    <p>{{ directorInfo }}</p>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import { useRouter, useRoute } from 'vue-router';
const router = useRouter()
const store = useCounterStore()
const route = useRoute()

console.log(route.params.directorid);

const directorInfo = ref({})

onMounted(() => {
  axios({
      method:'get',
      url : `https://api.themoviedb.org/3/person/${route.params.directorid}`,
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${store.TMDB_KEY}`
        }
    })
    .then((res) =>{
      // console.log(res.data);
      directorInfo.value = res.data
    })
})
</script>

<style scoped>

</style>