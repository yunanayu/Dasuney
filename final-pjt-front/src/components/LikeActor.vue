<template>
  <div>
    <div class="director-info" @click.prevent="goDetail(actorInfo.name)">
      <img :src="(`https://image.tmdb.org/t/p/w500/${actorInfo.profile_path}`)" alt="">
      <p> {{ actorInfo.name }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import { useRouter } from 'vue-router';

const router = useRouter();
const store = useCounterStore()
const props = defineProps ({
  actor : Object
})

const actorInfo = ref({})

const goDetail = function (actorname) {
  router.push({
    name: 'actormovielist',
    params: { actorid: actorInfo.value.id },
    query: { actorname: actorname }
  })
}


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
      actorInfo.value = res.data
    })
})
</script>

<style scoped>
.director-info {
  cursor: pointer;
}

img {
  width: 200px;
  height: 250px;
}

img:hover {
  /* 여기에 원하는 호버 효과 스타일을 추가하세요 */
  border: 4px solid beige
  /* 예: 테두리 추가 */
}
</style>