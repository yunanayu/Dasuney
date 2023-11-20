<template>
  <div>
    <!-- <p>영화</p> -->
    <img :src="movieDetail.poster_path" alt="">
    {{ movieDetail }}
    <span @click="goMovieDetail(movieDetail.movie_id)">제목 : {{ movieDetail.title }}</span>
    <button @click.prevent="likeMovie(movieDetail.id)">zz</button>
    <hr>
  </div>
</template>

<script setup>
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useCounterStore } from '../stores/counter';
const store = useCounterStore()
const router = useRouter()
const props = defineProps({
  movieDetail : Object
})

const goMovieDetail = function (movieId) {
  router.push({name:'moviedetail', params:{ movieId: movieId }})
}
// 영화 좋아요
const likeMovie = function (movieId) {
  axios({
    method : 'post',
    url : `http://127.0.0.1:8000/movies/${movieId}/movielike/`,
    headers : {
      Authorization:`Token ${store.Token}`
    }
  })
  .then((res) => {
    console.log(res)
  })
  .catch(err => console.log(err))
}
</script>

<style scoped>

</style>