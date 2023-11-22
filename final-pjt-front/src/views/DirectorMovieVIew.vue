<template>
  <div>
    <h1>갬동님이 참여한 영화 상세정보 페이지 입니당....</h1>
    <img :src="(`https://image.tmdb.org/t/p/w500/${directorInfo.profile_path}`)" alt="">
    <p> 이름 : {{ route.query.directorname }}</p>
    <button @click.prevent="likeDirector(directorInfo.name)">{{ isLiked ? '안조하여':'조아혀???'}}</button>
    <!-- <p>{{ directorInfo }}</p> -->
    <div v-for="credit in directorCredits">
      <!-- {{ credit }} -->
      <img :src="(`https://image.tmdb.org/t/p/w500/${credit.poster_path}`)" alt="">
      <p>제목 : {{ credit.title }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import { useRouter, useRoute } from 'vue-router';
const router = useRouter()
const store = useCounterStore()
const route = useRoute()

// console.log(route.params.directorid);
console.log(route.query.directorname);
const directorInfo = ref({})

const directorCredits = ref([])

const isLiked = ref(false)
const likeDirector = function (directorname) {
  const director = store.directors.find((director) => director.director_name === directorname)
  axios({
      method : 'post',
      url : `http://127.0.0.1:8000/movies/director/${director.id}/directorlike/`,
      headers : {
        Authorization:`Token ${store.Token}`
      }
    })
    .then((res) => {
      console.log(res.data)
      isLiked.value = res.data.is_liked
    })
    .catch(err => console.log(err))
  }



onMounted(() => {
  axios({
      method:'get',
      url : `https://api.themoviedb.org/3/person/${route.params.directorid}`,
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${store.TMDB_KEY}`
        }
    })
    .then((res) =>{
      // console.log(res.data);
      directorInfo.value = res.data
    })

  axios({
      method:'get',
      url : `https://api.themoviedb.org/3/person/${route.params.directorid}/movie_credits?language=ko-KR`,
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${store.TMDB_KEY}`
        }
    })
    .then((res) =>{
      // console.log(res.data.crew);
      const credits = res.data.crew.filter((crew) => crew.job == 'Director' && crew.overview != '')
      directorCredits.value = credits
      // console.log(credits)
      
    })


  const director = store.directors.find((director) => director.director_id == route.params.directorid)
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/movies/director/${director.id}/directorlike/`,
    headers : {
      Authorization:`Token ${store.Token}`
    }
  })
  .then((res) => {
    isLiked.value = res.data.is_liked
  })
  .catch(err => console.log(err))
})


</script>

<style scoped>

</style>