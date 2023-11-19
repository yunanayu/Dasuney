<template>
  <div>
    <h1>영화 리스트</h1>
    <MovieCard v-for="movie in movies" :movie-detail="movie"/>
  </div>
</template>

<script setup>
import MovieCard from '@/components/MovieCard.vue'
import { onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import { ref } from 'vue';
import axios from 'axios';
// const movies = ref([])
const store = useCounterStore()
defineProps({
  movies:Array
})
// onMounted(()=>{
//   axios({
//     method : 'get',
//     url : 'http://127.0.0.1:8000/movies/',
//     headers : {
//       Authorization:`Token ${store.Token}`
//     }
//     .then((res) => {
//       console.log(res.data);
//     })
//   })
// })
</script>

<style scoped>

</style>