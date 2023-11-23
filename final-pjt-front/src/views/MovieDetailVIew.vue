<template>
  <div class="container">
    <div v-if="movieDetail">
      <div v-if="movieDetail">
        <MovieInfo :movie-info="movieDetail"/>
        <div style="margin-left: 270px;">
          <h3>리뷰 목록</h3>
        </div>
        <div v-if="movieReviews">
          <ReviewCard  v-for="review in movieReviews" :review="review"/>
        </div>
      </div>
      <div style="margin-left: 270px;">
        <h3>감독</h3>
      </div>
      <div class="director">
        <Director v-for="director in directors" :director="director"/>
      </div>
      <hr>
      <div style="margin-left: 270px;">
      <h3>배우</h3>
      </div>
      <div class="actor">
        <Actor v-for="cast in casts" :cast="cast"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import ReviewCard from '../components/community/ReviewCard.vue';
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '../stores/counter';
import MovieInfo from '../components/MovieInfo.vue';
import Actor from '../components/Actor.vue';
import Director from '../components/Director.vue';


const store = useCounterStore()
const route = useRoute()
const key = import.meta.env.VITE_TMDB_API_KEY
const movieDetail = ref(null)
const casts = ref([])
const directors = ref({})
// console.log(route.params);
const movieReviews = ref([])

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
      casts.value = res.data.cast.slice(0,5)
      directors.value = res.data.crew.filter((crew)=>crew.job === 'Director')
    })
    .catch(err=>console.log(err))
    const moviePk = store.movies.find((movie) => movie.movie_id == route.params.movieId)
    if (moviePk) {
      axios({
        method : 'get',
        url : `http://127.0.0.1:8000/community/reviews/movie/${moviePk.id}/`,
        headers: {
            Authorization: `Token ${store.Token}`
          },
      })
      .then((res)=>{
        // console.log(res.data);
        movieReviews.value = res.data
      })
      .catch((err)=>console.log(err))
    } else {
      
    }
})
</script>

<style scoped>
.actor {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  margin-left: 240px;
}

</style>