<template>
  <div class="banner">
    <div class="content">
      <h1>{{ movieTitle.title }}</h1>
      <br>
      <p>시골에 사는 소녀 미츠하(가미시라이시 모네)는 어느 날 잠에서 깬 후 자신의 몸이 남자로 바뀐 걸 알게 된다.<br> 같은 시간, 도쿄에 사는 소년 타키(가미키 류노스케) 역시 이 기이한 상황을 겪고 있다.<br>  언제부턴가 더 이상 몸이 바뀌지 않자 자신들이 특별하게 이어져있었음을 깨달은 타키는 미츠하를 만나러 가는데...</p>
    </div>
  </div>
  <div class="back">
    <div class="container">
      <MovieList :movies="store.movies"/>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import MovieList from '@/components/MovieList.vue';
import { useCounterStore } from '../stores/counter';
import { ref } from 'vue';
import axios from 'axios';
const store = useCounterStore()

onMounted(()=>{
  window.resizeTo(1000, 1000)
  store.getMovieList()
  store.getActors()
  store.getDirectors()

})
const movieTitle = store.movies.find((movie) => movie.title === '너의 이름은.')
console.log(movieTitle)
</script>


<style scoped>

.background-image {
  /* position: fixed; */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}

.banner {
  position: relative;
  background-image: linear-gradient(to top, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0)), url("@/assets/yourname.jpg");
  background-color: #0b1035;
  background-size: 1900px 700px;
  background-repeat: no-repeat;
  height: 700px;
  position: relative;
}
.content {
  /* 내용을 여기에 추가하세요 */
  padding: 40px;
  position: absolute;
  top: 400px;
  font-size: 15px;
  /* 추가적인 스타일을 필요에 따라 설정하세요 */
}

.back {
  background-color: rgb(2, 2, 12);
}

.container {
  width: 4000px;
}
</style>