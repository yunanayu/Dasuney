<template>
<div>
  <div id="movieCarousel" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner" style="position: relative;">
      <h1 style="position: absolute; top: 50px; left: 100px;">평점 순위별 영화</h1>
      <div v-for="(movie, index) in chunkedMovies" :key="index" :class="{ 'carousel-item': true, 'active': index === 0 }">
        <MovieCard :movie-detail="movie" />
      </div>
    </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#movieCarousel" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">이전</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#movieCarousel" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">다음</span>
    </button>
  </div>``
</div>
</template>

<script setup>
import MovieCard from '@/components/MovieCard.vue'
import { onMounted, ref, defineProps, computed } from 'vue';
import { useCounterStore } from '../stores/counter';
import axios from 'axios';
// const movies = ref([])
const store = useCounterStore()
const props = defineProps({
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
const chunkedMovies = computed(() => {
  return Array.from({length: Math.ceil(props.movies.length / 4)}, (v,i)=>
    props.movies.slice(i * 4, i* 4 + 4)
  )
})
</script>

<style scoped>

.carousel-inner {
  text-align: center;
}


</style>