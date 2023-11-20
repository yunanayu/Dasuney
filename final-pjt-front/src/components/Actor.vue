<template>
  <div>
    <p>{{ cast }}</p>
    <p>{{ cast.name }}</p>
    <p>{{ cast.id }}</p>
    <button @click.prevent="likeActor(cast.id)">좋아여</button>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';

const store = useCounterStore()
defineProps({
  cast:Object
})


const likeActor = function (actorId) {
  axios({
    method : 'post',
    url : `http://127.0.0.1:8000/movies/actor/${actorId}/actorlike/`,
    headers : {
      Authorization:`Token ${store.Token}`
    }
  })
  .then((res) => {
    console.log(res)
  })
  .catch(err => console.log(err))
}
</script>

<style scoped>

</style>