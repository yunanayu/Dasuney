<template>
  <div class="container">
    <h1 style="margin-top: 20px;">{{ route.params.username }}님의 평가</h1>
    <h6>평가가 많을수록 {{ route.params.username }}님에게 맞는 영화를 추천해드려요 </h6>
    <div class="array">
      <HopeMovieCard 
      v-for="movie in ratingMovies"
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
const route = useRoute()
const store = useCounterStore()

// console.log(route.params)
const ratingMovies = ref([])

onMounted(() => {
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/accounts/profile/${route.params.username}/`,
    headers : {
        Authorization:`Token ${store.Token}`
      }
  })
  .then((res) => {;
    // console.log(res.data.score_set);
    ratingMovies.value = res.data.score_set
    console.log(ratingMovies.value);
  })
  .catch(err=>console.log(err))
});
</script>

<style scoped>
.array{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-auto-rows: 350px;
  grid-gap: 10px;
  margin-top: 20px;
}
</style>
