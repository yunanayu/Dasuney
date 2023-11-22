<template>
  <div class="container">
    <div v-if="director" class="director-detail">
      <img :src="(`https://image.tmdb.org/t/p/w500/${director.profile_path}`)" alt="감독 프로필">
      <div class="director-info">
        <p>{{ director.name }}</p>
        <p>{{ director.id }}</p>
        <button @click.prevent="likeDirector(director.name)">{{ isLiked ? '좋아요 취소' : '좋아요'}}</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
const store = useCounterStore()
const props = defineProps({
  director:Object
})
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
  const director = store.directors.find((director) => director.director_name == props.director.name)
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
</script>

<style scoped>
.director-detail {
  font-family: 'Arial', sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
.director-detail img {
  max-width: 200px;
  margin-right: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
} 
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
</style>
