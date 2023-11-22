<!-- 인기도?암틈 걔가 60점 이상이면 뽑아왔어요... -->
<template>
  <div>
    <h1>{{ route.query.actorname }} 참여한 영화 상세정보 페이지 입니당....</h1>
    <img :src="(`https://image.tmdb.org/t/p/w500/${actorInfo.profile_path}`)" alt="">
    <p> 이름 : {{ route.query.actorname }}</p>
    <button @click.prevent="likeActor(actorInfo.name)">{{ isLiked ? '안조하여':'조아혀???'}}</button>
    <!-- <p>{{ directorInfo }}</p> -->
    <div v-for="credit in actorCredits">
      <!-- {{ credit }} -->
      <img :src="(`https://image.tmdb.org/t/p/w500/${credit.poster_path}`)" alt="">
      <p>{{ credit }}</p>
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

// console.log(route.params.actorid);
// console.log(route.query.actorname);
const actorInfo = ref({})

const actorCredits = ref([])

const isLiked = ref(false)
const likeActor = function (actorname) {
  const actor = store.actors.find((actor) => actor.actor_name == actorname)
  console.log(actor)
  axios({
    method : 'post',
    url : `http://127.0.0.1:8000/movies/actor/${actor.id}/actorlike/`,
    headers : {
      Authorization:`Token ${store.Token}`
    }
  })
  .then((res) => {
    // console.log(res.data)
    isLiked.value = res.data.is_liked
  })
  .catch(err => console.log(err))
  }




onMounted(() => {
  axios({
      method:'get',
      url : `https://api.themoviedb.org/3/person/${route.params.actorid}`,
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${store.TMDB_KEY}`
        }
    })
    .then((res) =>{
      // console.log(res.data);
      actorInfo.value = res.data
    })

  axios({
      method:'get',
      url : `https://api.themoviedb.org/3/person/${route.params.actorid}/movie_credits?language=ko-KR`,
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${store.TMDB_KEY}`
        }
    })
    .then((res) =>{
      // console.log(res.data.cast);
      const credits = res.data.cast.filter((cast) => cast.popularity > 60 && cast.overview != '')
      actorCredits.value = credits
      console.log(credits)
      
    })


  const actor = store.actors.find((actor) => actor.actor_id == route.params.actorid)
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/movies/director/${actor.id}/directorlike/`,
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