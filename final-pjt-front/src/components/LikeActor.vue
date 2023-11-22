<template>
  <div>
    <br>
    <img :src="(`https://image.tmdb.org/t/p/w500/${actorInfo.profile_path}`)" alt="">
    <p> {{ actorInfo.name }}</p>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';

const store = useCounterStore()
const props = defineProps ({
  actor : Object
})

const actorInfo = ref({})

onMounted(() => {
  axios({
      method:'get',
      url : `https://api.themoviedb.org/3/person/${props.actor.actor_id}`,
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${store.TMDB_KEY}`
        }
    })
    .then((res) =>{
      // console.log(res.data);
      actorInfo.value = res.data
    })
})
</script>

<style scoped>
img {
  width: 200px;
  height: 250px;
}

img:hover {
  /* 여기에 원하는 호버 효과 스타일을 추가하세요 */
  border: 4px solid beige
  /* 예: 테두리 추가 */
}

p {
  text-align: center;
  margin-right: 20px;
  margin-top: 10px;
}

</style>