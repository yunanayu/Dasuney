<template>
  <div>
    <h1>영화 리스트</h1>
    <div class="swiper-container">
      <div class="swiper-wrapper">
        <MovieCard v-for="movie in movies" :key="movie.id" :movie-detail="movie" class="swiper-slide" />
      </div>
      <div class="swiper-pagination"></div>
      <div class="swiper-button-next"></div>
      <div class="swiper-button-prev"></div>
    </div>
  </div>
</template>

<script setup>
import MovieCard from '@/components/MovieCard.vue'
import { defineProps, onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import { ref } from 'vue';
import axios from 'axios';
import Swiper from 'swiper';

// const movies = ref([])
const store = useCounterStore()
defineProps({
  movies:Array
})

onMounted(() => {
  new Swiper('.swiper-container', {
    slidesPerView: 4,
    spaceBetween: 15,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  });
});
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
.array {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 300px;
  grid-gap: 15px;
  padding: 15px;
}
</style>