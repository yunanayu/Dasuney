<template>
  <div>
    <h1>영화 상세 정보 페이지</h1>
    <div v-if="movieDetail">
      <MovieInfo :movie-info="movieDetail"/>
    </div>
    <h3>Credits</h3>
    <h4>출연진</h4>
    <Actor v-for="cast in casts" :cast="cast"/>
    <hr>
    <h5>감독</h5>
    <Director v-for="director in directors" :director="director"/>

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
// const store = useCounterStore()
const key = import.meta.env.VITE_TMDB_API_KEY
const movieDetail = ref(null)
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
    movieDetail.value = res.data
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
      casts.value = res.data.cast.slice(0,5)
      directors.value = res.data.crew.filter((crew)=>crew.job === 'Director')
    })
    .catch(err=>console.log(err))
  
})
</script>

<style scoped>

</style>