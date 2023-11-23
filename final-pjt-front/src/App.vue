<script setup>
import axios from 'axios';
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from './stores/counter';
import { useRouter } from 'vue-router';
import { ref } from 'vue';
const store = useCounterStore()
const router = useRouter()
const search = ref('')
const goDetail = function () {
  const searchMovie = store.movies.find((movie) => movie.title == search.value)
  // console.log(searchMovie);
  router.push({name:'moviedetail', params:{movieId:searchMovie.movie_id}})
  search.value = ''
}
</script>

<template>
  <div id="app">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark navtext" v-show="store.navshow">
        <div class="container">
          <RouterLink class="navbar-brand" to="/home" style="font-size: 40px;" v-show="store.isAuthenticated">Dasuney+</RouterLink>
          <RouterLink class="navbar-brand" to="/intro" style="font-size: 40px;" v-show="!store.isAuthenticated">Dasuney+</RouterLink>
        
        <div class="nav-item me-auto" v-if="store.isAuthenticated">
          <RouterLink class="nav-link" :to="{name:'profile',params:{username:store.tempUsername}}" style="font-size: 30px;">Profile</RouterLink>
        </div>
        <!-- 검색기능입니당 우하하 -->
        <div>
          <div class="search">
            <form class="form-inline my-2 my-lg-0" @submit.prevent="goDetail">
          <div class="input-group">
            <input class="form-control textarea" type="search" placeholder="영화 제목을 입력 해 주세요." aria-label="Search" id="searchInput" v-model="search">
            <div class="input-group-append">
              <button class="btn btn-outline-success my-2 my-sm-0" type="button">🔍</button>
            </div>
          </div>
        </form>
          </div>
        </div>
        </div>
        <div class="collapse navbar-collapse" id="navbarNav"></div>
        <!-- 로그아웃 버튼은 화면이 작아졌을 때도 보이게 설정 -->
        <button class="btn btn-outline-light" @click.prevent="store.logout()" v-if="store.isAuthenticated" style="font-size: 20px;">LogOut</button>
      </nav>
      <RouterView />

      <!-- <footer class="footer fixed-bottom">
        <div class="container">
          <div class="row">
            <div class="col-md-4">
              <p>&copy; Dasuney+ 문신웅 | 정유나</p>
            </div>

            <div class="col-md-4 text-md-end">
              <a href="#" style="font-size: 30px;">🔍</a>
            </div>
          </div>
        </div>
      </footer> -->
    </div>
</template>

<style scoped>
#app {
  background-color: #0b1035;
  font-family: 'Arial', sans-serif;
  color: white;
}
.navtext {
  font-family: disney;
  /* font-size: 30px; */
}
.navbar-brand {
  margin-left: 15px;
}
.btn-outline-light {
  margin-right: 20px;
  font-family: 'Arial', sans-serif;
}
.nav-link {
  text-align: left;
}

.footer {
  background-color: #0b1f35;
  padding: 10px 0;
  /* margin-bottom: 20px; */
  color: white;
  height: 50px;
  display: flex;
  flex-direction: space-between;
}

.footer a {
  color: white;
  text-decoration: underline;
}

.footer a:hover {
  color: #ddd;
}
.search {
  width: 400px;
  font-size: 20px;
  font-family: 'Arial', sans-serif;
}
</style>
