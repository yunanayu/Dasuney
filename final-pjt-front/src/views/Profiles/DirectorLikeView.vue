<template>
  <div class="container">
    <h1 class="pageTitle">{{ route.params.username }}님이 좋아하는 감독</h1>
    <h6 class="subtitle">감독을 클릭하면 출연작을 볼 수 있어요</h6>
    <div class="array">
      <LikeDirector v-for="director in LikeDirectors" :key="director.director_id" :director="director"/>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '../../stores/counter';
import LikeDirector from '../../components/LikeDirector.vue';
import axios from 'axios';

const route = useRoute();
const store = useCounterStore();
const LikeDirectors = ref([]);

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/accounts/profile/${route.params.username}/`,
    headers: {
      Authorization: `Token ${store.Token}`
    }
  })
    .then((res) => {
      LikeDirectors.value = res.data.like_director;
    })
    .catch((err) => console.log(err));
});
</script>

<style scoped>
.container {
  padding: 20px;
  background-color: #2b2b2b;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-top: 10px;
}

.pageTitle {
  font-size: 50px;
  color: #d9d8d8;
}
.subtitle {
  font-size: 20px;
  color: #989696;
}
.array {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-rows: 300px;
  grid-gap: 20px;
}
</style>
