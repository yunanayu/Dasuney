<template>
  <div class="banner">
    <div class="content">
      <h1>{{ movieTitle.title }}</h1>
      <br />
      <p>
        시골에 사는 소녀 미츠하(가미시라이시 모네)는 어느 날 잠에서 깬 후 자신의 몸이 남자로
        바뀐 걸 알게 된다.<br /> 같은 시간, 도쿄에 사는 소년 타키(가미키 류노스케) 역시 이 기이한
        상황을 겪고 있다.<br /> 언제부턴가 더 이상 몸이 바뀌지 않자 자신들이 특별하게
        이어져있었음을 깨달은 타키는 미츠하를 만나러 가는데...
      </p>
      <div class="ready-player-1">
        <audio crossorigin preload="none">
          <source src="@/assets/yourname.mp3" type="audio/mp3" />
          지원하지 않는 브라우저입니다.
        </audio>
      </div>
    </div>
  </div>
  <div class="back">
    <div class="container" style="position: relative;">
      <h2 style="position: absolute; top: 50px; left: 5px;">최신 영화</h2>
      <MovieList :movies="releaseMovies" />
    </div>
  </div>
  <div class="back">
    <div class="container" style="position: relative;">
      <h2 style="position: absolute; top: 50px; left: 5px;">인기 영화</h2>
      <MovieList :movies="popularityMovies" />
    </div>
  </div>
  <div class="back">
    <div class="container" style="position: relative;">
      <h2 style="position: absolute; top: 50px; left: 5px;">평점 순위별 영화</h2>
      <MovieList :movies="store.movies" />
    </div>
  </div>
  <div class="back" v-if="reviewRecommend">
    <div class="container" style="position: relative;">
      <h2 style="position: absolute; top: 50px; left: 5px;">{{ store.tempUsername }}님을 위한 추천 영화</h2>
      <MovieList :movies="reviewRecommend" />
    </div>
  </div>
  <div class="back" v-if="likeRecommend">
    <div class="container" style="position: relative;">
      <h2 style="position: absolute; top: 50px; left: 5px;">{{ store.tempUsername }}님과 취향이 비슷한 사용자들이 보고싶은 영화</h2>
      <MovieList :movies="likeRecommend" />
    </div>
  </div>
</template>


<script>
document.addEventListener('DOMContentLoaded', function() {
  new GreenAudioPlayer('.ready-player-1',
          { showTooltips: true,  
          enableKeystrokes: true 
          }
      );
      
    });



</script>
<script setup>
import { ref, onMounted } from 'vue';
import MovieList from '@/components/MovieList.vue';
import { useCounterStore } from '../stores/counter';
import axios from 'axios';

const store = useCounterStore();
const releaseMovies = ref([])
const popularityMovies = ref([])
const reviewRecommend = ref([])
const likeRecommend = ref([])
onMounted(() => {
  window.resizeTo(1000, 1000);
  store.getMovieList();
  store.getActors();
  store.getDirectors();

  // c최신 개봉순
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/movies/sort/2/`,
    headers : {
        Authorization:`Token ${store.Token}`
      }
  })
  .then((res) => {
    // console.log(res.data)
    releaseMovies.value = res.data
  })
  .catch(err=>console.log(err))

  // 인기순
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/movies/sort/1/`,
    headers : {
        Authorization:`Token ${store.Token}`
      }
  })
  .then((res) => {
    // console.log(res.data)
    popularityMovies.value = res.data
  })
  .catch(err=>console.log(err))
  

  // 사용자 리뷰와 평점 좋아요 사용한 알고리즘 추천
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/movies/reviewlikerecommend/`,
    headers : {
        Authorization:`Token ${store.Token}`
      }
    })
    .then((res) => {
      console.log(res.data)
      reviewRecommend.value = res.data
    })
    .catch(err=>console.log(err))


    // 좋아요 유사 사용자
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/movies/similaruserrecommend/`,
    headers : {
        Authorization:`Token ${store.Token}`
      }
    })
    .then((res) => {
      console.log(res.data)
      likeRecommend.value = res.data
    })
    .catch(err=>console.log(err))
});

const movieTitle = store.movies.find((movie) => movie.title === '너의 이름은.');
</script>

<style scoped>
.background-image {
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}

.banner {
  position: relative;
  background-image: linear-gradient(to top, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0)),
    url("@/assets/yourname.jpg");
  background-color: #0b1035;
  background-size: 1900px 700px;
  background-repeat: no-repeat;
  height: 700px;
  position: relative;
}
.content {
  padding: 40px;
  position: absolute;
  top: 400px;
  font-size: 15px;
}

.back {
  background-color: rgb(2, 2, 12);
}

.container {
  width: 4000px;
}
.ready-player-1 {
  background-color: transparent;
}
</style>
