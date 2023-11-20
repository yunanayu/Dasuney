<template>
  <div>
    <p>{{ cast }}</p>
    <p>{{ cast.name }}</p>
    <p>{{ cast.id }}</p>
    <button @click.prevent="likeActor(cast.name)">좋아요</button>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import { storeToRefs } from 'pinia';

const store = useCounterStore()
const props = defineProps({
  cast:Object
})

const likeActor = function (actorname) {
    const actor = store.actors.find((actor) => actor.actor_name == actorname)
    axios({
      method : 'post',
      url : `http://127.0.0.1:8000/movies/actor/${actor.id}/actorlike/`,
      headers : {
        Authorization:`Token ${store.Token}`
      }
    })
    .then((res) => {
      // const actor = store.actors.find((actor) => actor.name === props.cast.name)
      console.log(res)
      // console.log(actor)
    })
    .catch(err => console.log(err))
  }
</script>

<style scoped>

</style>