<template>
<div>
  <h1>평점 순위별 영화 추천 </h1>
  <div id="movieCarousel" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">
      <div v-for="(movie, index) in movies" :key="index" :class="{ 'carousel-item': true, 'active': index === 0 }">
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
  </div>
</div>
</template>

<script setup>
import MovieCard from '@/components/MovieCard.vue'
import { onMounted, ref, defineProps } from 'vue';
import { useCounterStore } from '../stores/counter';
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
/* .array {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 300px;
  grid-gap: 15px;
  padding: 15px;
} */
.carousel-inner {
  text-align: center;
}
</style>