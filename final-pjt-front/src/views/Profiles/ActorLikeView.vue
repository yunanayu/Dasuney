<template>
  <div>
    <h3>좋아하는 배우 LIST</h3>
    <LikeActor v-for="actor in LikeActors" :actor="actor"/>
    <!-- <Actor v-for="actor in LikeActors" :cast="actor"/> -->
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import LikeActor from '@/components/LikeActor.vue'
import Actor from '../../components/Actor.vue';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';
const route = useRoute()
const store = useCounterStore()

const LikeActors = ref([])

onMounted(() => {
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/accounts/profile/${route.params.username}/`,
    headers : {
        Authorization:`Token ${store.Token}`
      }
  })
  .then((res) => {;
    LikeActors.value = res.data.like_actor
    // console.log(LikeActors.value);
  })
  .catch(err=>console.log(err))
});
</script>

<style scoped>

</style>