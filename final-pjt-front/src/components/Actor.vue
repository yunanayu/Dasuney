<template>
  <div class="container">
    <div class="actor-detail">
      <div class="grid">
          <img :src="(`https://image.tmdb.org/t/p/w500/${cast.profile_path}`)" alt="배우 포스터"  @click.prevent="goDetail(cast.name)">
        <div class="actor-info">
          <p>{{ cast.name }}</p>
          <!-- <p>{{ cast.id }}</p> -->
          <button @click.prevent="likeActor(cast.name)">{{ isLiked ? '좋아요 취소':'배우 좋아요'}}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import { useRouter } from 'vue-router';
const router = useRouter()
const store = useCounterStore()
const props = defineProps({
  cast:Object
})
const isLiked = ref(false)
const goDetail = function (actorname) {
  const actor = store.actors.find((actor) => actor.actor_name === actorname)
  console.log(actor)
  router.push({name:'actormovielist', params : {actorid : actor.actor_id}, query : {actorname : actorname}})
}

const likeActor = function (actorname) {
    const actor = store.actors.find((actor) => actor.actor_name == actorname)
    console.log(actor);
    axios({
      method : 'post',
      url : `http://127.0.0.1:8000/movies/actor/${actor.id}/actorlike/`,
      headers : {
        Authorization:`Token ${store.Token}`
      }
    })
    .then((res) => {
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
.actor-detail {
  display: flex;
  align-items: center;
  font-family: 'Arial', sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  
}

.actor-detail img {
  max-width: 200px;
  margin-right: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.actor-info {
  color: #f6f5f5;
}

.actor-info p {
  margin: 5px 0;
}

.actor-info button {
  background-color: #3498db;
  color: #fff;
  padding: 10px 15px;
  font-size: 1em;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.actor-info button:hover {
  background-color: #2980b9;
}
</style>
