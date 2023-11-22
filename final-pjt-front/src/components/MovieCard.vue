<template>
  <div>
    <div class="array">
      <div v-for="movie in movieDetail">
        <span @click="goMovieDetail(movie.movie_id)"><img :src="movie.poster_path" alt=""></span>
        
    </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useCounterStore } from '../stores/counter';
const store = useCounterStore()
const router = useRouter()
// const props = defineProps({
//   movieDetail : Array
// })
const { movieDetail } = defineProps(['movieDetail']);

const goMovieDetail = function (movieId) {
  router.push({name:'moviedetail', params:{ movieId: movieId }})
}

</script>

<style scoped>
img {
  width: 200px;
  height: 300px;
}

.array {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 400px;
  grid-gap: 15px;
  padding: 100px;
}
</style>