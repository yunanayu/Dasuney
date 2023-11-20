<template>
  <div>
    <!-- <p>영화</p> -->
    <img :src="movieDetail.poster_path" alt="">
    {{ movieDetail }}
    <span @click="goMovieDetail(movieDetail.movie_id)">제목 : {{ movieDetail.title }}</span>
    <hr>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()
const props = defineProps({
  movieDetail : Object
})

const goMovieDetail = function (movieId) {
  router.push({name:'moviedetail', params:{ movieId: movieId }})
}
</script>

<style scoped>

</style>