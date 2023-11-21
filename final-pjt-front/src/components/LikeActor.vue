<template>
  <div>
    <br>
    <img :src="(`https://image.tmdb.org/t/p/w500/${actorInfo.profile_path}`)" alt="">
    <p> 이름 : {{ actorInfo.name }}</p>
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

<style lang="scss" scoped>

</style>