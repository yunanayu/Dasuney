<template>
  <div>
    <h1>ㅁㅔ인페이지!으하하</h1>
    <MovieList :movies="movies"/>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import MovieList from '@/components/MovieList.vue';
import { useMovieStore } from '../stores/movie';
import { useCounterStore } from '../stores/counter';
import { ref } from 'vue';
import axios from 'axios';
const store = useCounterStore()
const movies = ref([])
// console.log(store.Token);
onMounted(()=>{
  // store.getMovieList
  axios({
      method : 'get',
      url : 'http://127.0.0.1:8000/movies/',
      headers : {
        Authorization:`Token ${store.Token}`
      }
      })
      .then((res) => {
        // console.log(res.data);
        movies.value = res.data
      })
      .catch(err=>console.log(err))
})

</script>


<style scoped>

</style>