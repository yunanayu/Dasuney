<template>
  <div>
    <h1>ㅁㅔ인페이지!으하하</h1>
    <MovieList :movies="movies"/>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import MovieList from '@/components/MovieList.vue';
import { useCounterStore } from '../stores/counter';
import { ref } from 'vue';
import axios from 'axios';
const store = useCounterStore()

// console.log(store.Token);

onMounted(()=>{
  window.resizeTo(1000, 1000)
  store.getMovieList()

  store.getActors()
  store.getDirectors()

})

</script>


<style scoped>

</style>