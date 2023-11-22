<template>
  <div>
    <h1> 제가 평점을 준 영화입니다요...하하...</h1>
  </div>
</template>

<script setup>
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

</style>
