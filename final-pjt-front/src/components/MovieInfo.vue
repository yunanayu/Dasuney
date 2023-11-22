<template>
  <div>
    <img :src="(`https://image.tmdb.org/t/p/w500/${movieInfo.poster_path}`)" alt="">
    <p>제목 : {{ movieInfo.title }}</p>
    <p>개봉일 : {{ movieInfo.release_date }}</p>
    <p>러닝타임 :{{ movieInfo.runtime }} 분</p>
    <p>TMDB 평점 : {{ movieInfo.vote_average }}</p>
    <h4>장르</h4>
    <p v-for="genre in movieInfo.genres">{{ genre.name }}</p>
    <h3>줄거리</h3>
    <p>{{ movieInfo.overview }}</p>
    <button @click.prevent="hopeMovie(movieInfo.title)">{{ isLiked ? '시류떡' : '조하여!!!!!!!!!!!!!!!!'}}</button>
    <hr>
    <div>
      <h3>평점 주기</h3>
      <ul>
        <li><a @click="reRateScore(0)" style="color:pink;">☆☆☆☆☆</a></li>
        <li><a @click="reRateScore(1)" style="color:pink;">★☆☆☆☆</a></li>
        <li><a @click="reRateScore(2)" style="color:pink;">★★☆☆☆</a></li>
        <li><a @click="reRateScore(3)" style="color:pink;">★★★☆☆</a></li>
        <li><a @click="reRateScore(4)" style="color:pink;">★★★★☆</a></li>
        <li><a @click="reRateScore(5)" style="color:pink;">★★★★★</a></li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
const store = useCounterStore()
const props = defineProps({
  movieInfo : Object
})
const isLiked = ref(false)
// 영화 좋아요
const hopeMovie = function (movietitle) {
  const movie = store.movies.find((movie) => movie.title === movietitle)
  axios({
    method : 'post',
    url : `http://127.0.0.1:8000/movies/${movie.id}/movielike/`,
    headers : {
      Authorization:`Token ${store.Token}`
    }
  })
  .then((res) => {
    // console.log(res.data.is_liked)
    isLiked.value = res.data.is_liked
  })
  .catch(err => console.log(err))
}


const reRateScore = function (score) {
  const movie = store.movies.find((movie) => movie.title == props.movieInfo.title)
  axios({
    method:'post',
    url : `http://127.0.0.1:8000/movies/${movie.id}/score/`,
    headers : {
      Authorization:`Token ${store.Token}`
    },
    data : {
      score : score
    }
  })
  .then ((res) => {
    console.log(res.data);
  })
}

onMounted(() => {
  const movie = store.movies.find((movie) => movie.title == props.movieInfo.title)
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/movies/${movie.id}/movielike/`,
    headers : {
      Authorization:`Token ${store.Token}`
    }
  })
  .then((res) => {
    // console.log(res.data.is_liked)
    isLiked.value = res.data.is_liked
  })
  .catch(err => console.log(err))
})

</script>

<style scoped>

</style>

