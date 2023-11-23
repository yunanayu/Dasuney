<template>
  <!-- <img class="background-image" src="@/assets/yourname.jpg" alt="yourname">
  <div class="content"> -->

    <div class="banner">
        <div class="bannerposition">
            <h1 class="dasney">Dasuney+ </h1><br>
            <h1>당신을 위한 영화를 <br>다 줄게요 <br></h1><br>
            <h5 style="color: gray;">지금 바로 회원이 되어보세요</h5>
          <div class="accounts">
            <router-link :to="{ name: 'login' }">
              <div class="email-container">
                <form class="email-form">
                  <div><button>로그인</button></div>
                </form>
              </div>
            </router-link>
            <router-link :to="{ name: 'signup' }">
              <div class="email-container">
                <form class="email-form">
                  <div><button>회원가입</button></div>
                </form>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    <MovieList :movies="store.movies"/>
  <!-- </div> -->
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

.content {
  /* 내용을 여기에 추가하세요 */
  padding: 40px;
  
  /* 추가적인 스타일을 필요에 따라 설정하세요 */
}
.banner {
  position: relative;
  background-image: linear-gradient(to right, rgba(0, 0, 0, 1.0), rgba(0, 0, 0, 0)), url("@/assets/lala.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  height: 900px;
  position: relative;
}
</style>