<!-- 인기도?암틈 걔가 60점 이상이면 뽑아왔어요... -->
<template>
  <div class="container">
    <div style="margin-top: 20px;">
      <h1>{{ route.query.actorname }} 배우님이 참여한 영화</h1>
      <div class="actor">
        <img :src="(`https://image.tmdb.org/t/p/w500/${actorInfo.profile_path}`)" alt="">
      </div>
      <h4>{{ route.query.actorname }}</h4>
      <div class="actor-info">
        <button @click.prevent="likeActor(actorInfo.name)">
          <!-- {{ isLiked ? '좋아요 취소':'좋아요'}}
           -->
           <span v-if="isLiked">💖</span>
            <span v-else>🤍</span>
        </button>
      </div>

      <div class="actor-movie" v-if="actorCredits">
        <div v-for="credit in actorCredits" @click="goDetail(credit.id)">
          <!-- {{ credit }}     -->
          <img :src="(`https://image.tmdb.org/t/p/w500/${credit.poster_path}`)" alt="">
          <p>{{ credit.title }}</p>
        </div>
      </div>
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
    console.log(res.data)
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
      const credits = res.data.cast.filter((cast) => cast.vote_average > 7 && cast.overview != '')
      actorCredits.value = credits
      console.log(credits)
      
    })


  const actor = store.actors.find((actor) => actor.actor_id == route.params.actorid)
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/movies/actor/${actor.id}/actorlike/`,
    headers : {
      Authorization:`Token ${store.Token}`
    }
  })
  .then((res) => {
    console.log(res.data)
    isLiked.value = res.data.is_liked
  })
  .catch(err => console.log(err))
})

const goDetail = function (movieId) {
  router.push({name:'moviedetail', params:{movieId:movieId}})
}
</script>

<style scoped>
.actor-info button {
  background-color: #3498db;
  color: #fff;
  padding: 10px 15px;
  font-size: 1em;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.actor-info button:hover {
  background-color: #2980b9;
}
.actor-movie {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-auto-rows: 350px;
  grid-gap: 40px;
  margin-top: 100px;
  text-align: center;
}
.actor-movie img {
  width: 200px;
  height: 300px;
}
.actor-movie img:hover {
  /* 여기에 원하는 호버 효과 스타일을 추가하세요 */
  border: 4px solid beige
  /* 예: 테두리 추가 */
}
.actor img {
  width: 300px;
  margin-top: 30px;
}
</style>