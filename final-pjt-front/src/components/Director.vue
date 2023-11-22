<template>
  <div v-if="director">
    <img :src="(`https://image.tmdb.org/t/p/w500/${director.profile_path}`)" alt="">
    <p>{{ director.name }}</p>
    <p>{{ director.id }}</p>
    <button @click.prevent="likeDirector(director.name)">{{ isLiked ? '안조하여':'조아혀???'}}</button>
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

</style>