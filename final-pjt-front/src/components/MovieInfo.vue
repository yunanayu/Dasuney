<template>
  <div>
    <img :src="(`https://image.tmdb.org/t/p/w500/${movieInfo.poster_path}`)" alt="">
    {{ movieInfo.id }}
    <p>제목 : {{ movieInfo.title }}</p>
    <p>개봉일 : {{ movieInfo.release_date }}</p>
    <p>러닝타임 :{{ movieInfo.runtime }} 분</p>
    <p>TMDB 평점 : {{ movieInfo.vote_average }}</p>
    <h4>장르</h4>
    <p v-for="genre in movieInfo.genres">{{ genre.name }}</p>
    <h3>줄거리</h3>
    <p>{{ movieInfo.overview }}</p>
    <button @click.prevent="hopeMovie(movieInfo.title)">조하여!!!!!!!!!!!!!!!!</button>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
const store = useCounterStore()
const props = defineProps({
  movieInfo:Object
})
const isLiked = ref(false)

const hopeMovie = function (title) {
  const movie = store
}
</script>

<style scoped>

</style>