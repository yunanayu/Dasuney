<template>
  <div>
    <h1>영화 상세 정보 페이지</h1>
    <!-- <p>{{ movieInfo }}</p> -->
    <MovieInfo :movie-info="movieInfo"/>
    <!-- <img :src="(`https://image.tmdb.org/t/p/w500/${movieInfo.poster_path}`)" alt="">
    <p>제목 : {{ movieInfo.title }}</p>
    <p>개봉일 : {{ movieInfo.release_date }}</p>
    <p>러닝타임 :{{ movieInfo.runtime }} 분</p>
    <p>TMDB 평점 : {{ movieInfo.vote_average }}</p>
    <h4>장르</h4>
    <p v-for="genre in movieInfo.genres">{{ genre.name }}</p>
    <h3>줄거리</h3>
    <p>{{ movieInfo.overview }}</p> -->
    <h3>Credits</h3>
    <Actor v-for="cast in casts" :cast="cast"/>
    <h4>출연진</h4>
    <!-- <h5>출연진</h5>
    <div v-for="cast in casts">
      <p>{{ cast.name }}</p>
      <p>{{ cast.id }}</p>
    </div> -->
    <hr>
    <Director v-for="director in directors"/>
    <h5>감독</h5>
    <!-- <h5>감독</h5>
    <div v-for="director in directors">
      {{ director }}
      <p>{{ director.name }}</p>
      <p>{{ director.id }}</p>
    </div> -->
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '../stores/counter';
import MovieInfo from '../components/MovieInfo.vue';
import Actor from '../components/Actor.vue';
import Director from '../components/Director.vue';

const route = useRoute()
const store = useCounterStore()
const key = import.meta.env.VITE_TMDB_API_KEY
const movieInfo = ref({})
const casts = ref([])
const directors = ref({})
// console.log(route.params);


onMounted(()=> {
  axios({
    method:'GET',
    url : `https://api.themoviedb.org/3/movie/${route.params.movieId}?language=ko-KR/`,
    headers: {
    accept: 'application/json',
    Authorization: `Bearer ${key}`
    }
  })
  .then((res)=>{
    // console.log(res.data);
    movieInfo.value = res.data
  })
  // store.getCredits(route.params.movieId)
  axios({
      method:'get',
      url : `https://api.themoviedb.org/3/movie/${route.params.movieId}/credits`,
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${key}`
        }
    })
    .then((res)=>{
      // console.log(res.data)
      // console.log(res.data.cast.slice(0,6));
      // console.log(res.data.crew.filter((crew)=>crew.job === 'Director'));
      casts.value = res.data.cast.slice(0,6)
      directors.value = res.data.crew.filter((crew)=>crew.job === 'Director')
    })
    .catch(err=>console.log(err))
  
})
</script>

<style scoped>

</style>