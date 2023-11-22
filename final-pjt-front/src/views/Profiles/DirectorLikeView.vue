<template>
  <div>
    <h3>좋아하는 갬동님 LIST</h3>
    <LikeDirector v-for="director in LikeDirectors" :director="director"/>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '../../stores/counter';
import LikeDirector from '../../components/LikeDirector.vue';
import axios from 'axios';
const route = useRoute()
const store = useCounterStore()

const LikeDirectors = ref([])

onMounted(() => {
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/accounts/profile/${route.params.username}/`,
    headers : {
        Authorization:`Token ${store.Token}`
      }
  })
  .then((res) => {;
    console.log(res.data);
    LikeDirectors.value = res.data.like_director
  })
  .catch(err=>console.log(err))
});
</script>

<style scoped>

</style>