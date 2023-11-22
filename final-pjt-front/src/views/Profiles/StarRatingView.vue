<template>
  <div class="container">
    <h1 class="pageTitle">{{ route.params.username }}님의 평가</h1>
    <h6 class="subtitle">평가가 많을수록 {{ route.params.username }}님에게 맞는 영화를 추천해드려요</h6>
    <div class="array">
      <HopeMovieCard 
        v-for="movie in ratingMovies"
        :key="movie.movie.movie_id"
        :movie-detail="movie.movie"
      />
    </div>
  </div>
</template>

<script setup>
import HopeMovieCard from '../../components/HopeMovieCard.vue';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';

const route = useRoute();
const store = useCounterStore();
const ratingMovies = ref([]);

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/accounts/profile/${route.params.username}/`,
    headers: {
      Authorization: `Token ${store.Token}`
    }
  })
    .then((res) => {
      ratingMovies.value = res.data.score_set;
    })
    .catch((err) => console.log(err));
});
</script>

<style scoped>
.container {
  padding: 20px;
  background-color: #2b2b2b;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-top: 10px;
}

.pageTitle {
  font-size: 50px;
  color: #d9d8d8;
}

.subtitle {
  font-size: 20px;
  color: #989696;
}

.array {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-auto-rows: 350px;
  grid-gap: 20px;
  margin-top: 20px;
  margin-left: 40px;
}
</style>
