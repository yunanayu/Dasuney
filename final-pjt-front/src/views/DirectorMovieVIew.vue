<template>
  <div class="container">
    <div style="margin-top: 20px;">
      <h1>감독님이 참여한 작품</h1>
      <div class="director">
        <img :src="(`https://image.tmdb.org/t/p/w500/${directorInfo.profile_path}`)" alt="">
      </div>
      <h4>{{ route.query.directorname }}</h4>
      <div class="director-info">
        <button @click.prevent="likeDirector(directorInfo.name)">
          <!-- {{ isLiked ? '좋아요 취소':'좋아요'}} -->
          <span v-if="isLiked">💖</span>
          <span v-else>🤍</span>
        </button>
      </div>
      
      <div class="dircetor-movie" v-if="directorCredits">
        <div v-for="credit in directorCredits" @click="goDetail(credit.id)">
          <img :src="(`https://image.tmdb.org/t/p/w500/${credit.poster_path}`)" alt="">
          <p>제목 : {{ credit.title }}</p>
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
      const credits = res.data.crew.filter((crew) => crew.job == 'Director' && crew.overview != '' && crew.vote_average > 7.693)
      directorCredits.value = credits
      console.log(credits)
      
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

const goDetail = function (movieId) {
  router.push({name:'moviedetail', params:{movieId:movieId}})
}

</script>

<style scoped>
.director-info button {
  background-color: #3498db;
  color: #fff;
  padding: 10px 15px;
  font-size: 1em;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.director-info button:hover {
  background-color: #2980b9;
}
.dircetor-movie {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-auto-rows: 350px;
  grid-gap: 40px;
  margin-top: 100px;
  text-align: center;
}
.dircetor-movie img {
  width: 200px;
}

.director img {
  width: 300px;
  margin-top: 30px;
}

.dircetor-movie img:hover {
  /* 여기에 원하는 호버 효과 스타일을 추가하세요 */
  border: 4px solid beige
  /* 예: 테두리 추가 */
}
</style>