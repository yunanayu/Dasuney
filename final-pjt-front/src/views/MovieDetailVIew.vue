<template>
  <div class="container">
    <div v-if="movieDetail">
      <div class="movie-details">
        <div class="movie-info">
          <MovieInfo :movie-info="movieDetail"/>
        </div>

        <div class="review-section">
          <div v-if="movieReviews">
            <div class="review" ref="reviewContainer">
              <h3 style="margin-left: 130px;">Review List</h3>
              <ReviewCard v-for="review in movieReviews" :review="review" :key="review.id" />
              <form @submit.prevent="createReview" class="message">
                <div class="input-group">
                  <label for="content"></label>
                  <textarea id="content" v-model="content" cols="35" rows="2" placeholder="리뷰를 작성 해 주세요." style="white-space: pre-line;"></textarea>
                  <button type="submit" class="review-button">💌</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
      <hr>
      <div style="margin-left: 30px;">
        <h3>감독</h3>
      </div>
      <div class="director">
        <Director v-for="director in directors" :director="director"/>
      </div>
      <hr>
      <div style="margin-left: 30px;">
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
import { useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '../stores/counter';
import MovieInfo from '../components/MovieInfo.vue';
import Actor from '../components/Actor.vue';
import Director from '../components/Director.vue';

const router = useRouter()
const store = useCounterStore()
const route = useRoute()
const key = import.meta.env.VITE_TMDB_API_KEY
const movieDetail = ref(null)
const casts = ref([])
const directors = ref({})
// const title = ref('')
const content = ref('')
// const moviePK = ref('')
// console.log(route.params);
const movieReviews = ref([])

// 리뷰 작성하기 버튼
// const goReviewCreate = function () {
//     const movie = store.movies.find((m) => m.title === movieDetail.value.title);
//     router.push({name:'reviewcreate', params : {movieid:movie.id}, query:{movie_id:movieDetail.value.id}})
//   }

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

// ㄹㅣ뷰 작성하기
const createReview = function () {
  const movie = store.movies.find((m) => m.title === movieDetail.value.title);
  axios({
    method : 'post',
    url : `http://127.0.0.1:8000/community/reviews/movie/${movie.id}/`,
    headers : {
        Authorization:`Token ${store.Token}`
      },
    data : {
      title :`${movieDetail.value.title} 리뷰`,
      content : content.value
    }
  })
  .then((res) => {
    // console.log(res.data)
    window.alert('리뷰 작성이 완료되었습니다.')
    movieReviews.value.push(res.data)
    // title.value = ''
    content.value = ''
    // router.push({name:'moviedetail', params : {movieId:route.query.movie_id}})
  })
  .catch((err) => {
    console.log(err)
    if (title.value == '') {
      window.alert('제목을 작성해주세요')
    } else if (content.value == '') {
      window.alert('내용을 작성해주세요')
    }
  })
}

</script>


<style scoped>
.actor {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  
}

.container {
  display: flex;
}

.movie-details {
  display: flex;
  justify-content: space-between;
}

.movie-info {
  flex: 2;
  margin-right: 20px; /* Adjust the margin as needed */
}

.review-section {
  flex: 1;
}
.review{
  margin-top: 70px;
  border: 1px solid ;
}
.input-group {
  margin-left: 30px;
  margin-bottom: 20px;
}
.input-group button {
  background-color: #3498db;
  color: #fff;
  padding: 10px 20px;
  font-size: 1em;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
  
}
.input-group button:hover{
  background-color: #2980b9;
}

</style>