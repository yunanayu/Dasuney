<template>
  <div>
    <!-- <img :src="(`https://image.tmdb.org/t/p/w500/${movieInfo.poster_path}`)" alt="">
    {{ movieInfo }}
    <p>제목 : {{ movieInfo.title }}</p>
    <p>개봉일 : {{ movieInfo.release_date }}</p>
    <p>러닝타임 :{{ movieInfo.runtime }} 분</p>
    <p>TMDB 평점 : {{ movieInfo.vote_average }}</p>
    <h4>장르</h4>
    <p v-for="genre in movieInfo.genres">{{ genre.name }}</p>
    <h3>줄거리</h3>
    <p>{{ movieInfo.overview }}</p>
    <button @click.prevent="hopeMovie(movieInfo.title)">조하여!!!!!!!!!!!!!!!!</button> -->
      <!-- {{ movie }} -->
      {{ movieTitle }}
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
const store = useCounterStore()
// const props = defineProps({
//   movie : {
//     type : Object
//   }
// })

const props = defineProps({
  movie : Object
})
const isLiked = ref(false)

// const hopeMovie = function (title) {
//   const movie = store
// }


// 영화 좋아요
// const hopeMovie = function (movietitle) {
//   const movie = store.movies.find((movie) => movie.title === movietitle)
//   console.log(movie.id)
//   console.log(movie)
//   axios({
//     method : 'post',
//     url : `http://127.0.0.1:8000/movies/${movie.id}/movielike/`,
//     headers : {
//       Authorization:`Token ${store.Token}`
//     }
//   })
//   .then((res) => {
//     console.log(res)
//   })
//   .catch(err => console.log(err))
// }
console.log(1,props.movie);
// console.log(props.movie);

onMounted(() => {
  // console.log(props);
  // console.log(props.movie);
  // const movie = store.movies.find((movie) => movie.title === props.movieInfo.title)
  // axios({
  //   method : 'get',
  //   url : `http://127.0.0.1:8000/movies/${movie.id}/movielike/`,
  //   headers : {
  //     Authorization:`Token ${store.Token}`
  //   }
  // })
  // .then((res) => {
  //   console.log(res)
  // })
  // .catch(err => console.log(err))
})

</script>

<style scoped>

</style>

