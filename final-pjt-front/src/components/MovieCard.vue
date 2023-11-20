<template>
  <div>
    <!-- <p>영화</p> -->
    
    <!-- {{ movieDetail }} -->
    <span @click="goMovieDetail(movieDetail.movie_id)"><img :src="movieDetail.poster_path" alt=""></span>
    <!-- 좋아요 상세 페이지로 옮겨주세요  -->
    <button @click.prevent="likeMovie(movieDetail.id)">zz</button>
    <!-- <hr> -->
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
img {
  width: 200px;
}

</style>