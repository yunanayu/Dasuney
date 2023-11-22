<template>
  <div>
    <!-- <p>{{ cast }}</p> -->
    <img :src="(`https://image.tmdb.org/t/p/w500/${cast.profile_path}`)" alt="">
    <p>{{ cast.name }}</p>
    <p>{{ cast.id }}</p>
    <button @click.prevent="likeActor(cast.name)">{{ isLiked ? '좋아요 취소':'배우 좋아요'}}</button>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';


const store = useCounterStore()
const props = defineProps({
  cast:Object
})
console.log(props.cast)

const isLiked = ref(false)

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
      console.log(res.data)
      isLiked.value = res.data.is_liked
      // console.log(actor)
    })
    .catch(err => console.log(err))
  }

  onMounted(() => {
    const actor = store.actors.find((actor) => actor.actor_name == props.cast.name)
    // console.log(actor.id)
    axios({
      method : 'get',
      url : `http://127.0.0.1:8000/movies/actor/${actor.id}/actorlike/`,
      headers : {
        Authorization:`Token ${store.Token}`
      }
    })
    .then((res) => {
      // console.log(res.data);
      isLiked.value = res.data.is_liked
    })
    .catch(err => console.log(err))
  })
</script>

<style scoped>

</style>

