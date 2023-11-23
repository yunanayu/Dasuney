<template>
  <div>
    <div id="movieCarousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="3000">
      <div class="carousel-inner" style="position: relative;">
        <h1 style="position: absolute; top: 50px; left: 100px;">평점 순위별 영화</h1>
        <div v-for="(movie, index) in chunkedMovies" :key="index" :class="{ 'carousel-item': true, 'active': index === 0 }">
          <MovieCard :movie-detail="movie" />
        </div>
      </div>
      <div class="carousel-controls">
        <button class="carousel-control-prev" type="button" data-bs-target="#movieCarousel" data-bs-slide="prev" @mouseover="showPrevButton = true" @mouseleave="showPrevButton = false">
          <span v-if="showPrevButton" class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">이전</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#movieCarousel" data-bs-slide="next" @mouseover="showNextButton = true" @mouseleave="showNextButton = false">
          <span v-if="showNextButton" class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">다음</span>
        </button>
      </div>
    </div>
  </div>
</template>


<script setup>
import MovieCard from '@/components/MovieCard.vue'
import { onMounted, ref, defineProps, computed } from 'vue';
import { useCounterStore } from '../stores/counter';
import axios from 'axios';

const store = useCounterStore()
const props = defineProps({
  movies:Array
})

const chunkedMovies = computed(() => {
  return Array.from({length: Math.ceil(props.movies.length / 8)}, (v,i)=>
    props.movies.slice(i * 8, i* 8 + 8)
  )
})

const showPrevButton = ref(false);
const showNextButton = ref(false);
</script>

<style scoped>

.carousel-inner {
  text-align: left;
}

.carousel-controls .carousel-control-prev-icon .carousel-control-next-icon {
  display: inline-block; 
}

.carousel-controls .d-none {
  display: none; /* Hide the icon when not needed */
}
.carousel-control-prev {
  height: 100px;
  width: 100px;
  margin-top: 200px;
  /* margin-left: 20px; */
}
.carousel-control-next {
  height: 100px;
  width: 100px;
  margin-top: 200px;
  /* margin-left: 100px; */
}
.carousel-control-prev:hover,
.carousel-control-next:hover {
  background-color: black; /* Change the background color on hover */
}

.carousel-item {
  
}
</style>