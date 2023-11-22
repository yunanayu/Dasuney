<template>
  <div>
    <div class="director-info" @click.prevent="goDetail(directorInfo.name)">
      <img :src="`https://image.tmdb.org/t/p/w500/${directorInfo.profile_path}`" alt="">
      <p>{{ directorInfo.name }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import { useRouter } from 'vue-router';

const router = useRouter();
const store = useCounterStore();
const props = defineProps({
  director: Object
});

const directorInfo = ref({});

onMounted(() => {
  axios({
    method: 'get',
    url: `https://api.themoviedb.org/3/person/${props.director.director_id}`,
    headers: {
      accept: 'application/json',
      Authorization: `Bearer ${store.TMDB_KEY}`
    }
  })
    .then((res) => {
      directorInfo.value = res.data;
    });
});

const goDetail = function (directorname) {
  router.push({
    name: 'directormovielist',
    params: { directorid: directorInfo.value.id },
    query: { directorname: directorname }
  });
};
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
