<template>
  <div>
    <br>
    <img :src="(`https://image.tmdb.org/t/p/w500/${directorInfo.profile_path}`)" alt="">
    <p> 이름 : {{ directorInfo.name }}</p>
    {{ directorInfo }}
  </div>
  <hr>
  <span @click.prevent="goDetail(directorInfo.name)">상세 정보 보기</span>
  <hr>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import { useRouter } from 'vue-router';
const router = useRouter()
const store = useCounterStore()
const props = defineProps ({
  director : Object
})

const directorInfo = ref({})

onMounted(() => {
  axios({
      method:'get',
      url : `https://api.themoviedb.org/3/person/${props.director.director_id}`,
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${store.TMDB_KEY}`
        }
    })
    .then((res) =>{
      // console.log(res.data);
      directorInfo.value = res.data
    })
})

const goDetail = function (directorname) {
  router.push({name:'directormovielist', params:{directorid:directorInfo.value.id}, query:{directorname:directorname}})
}
</script>

<style lang="scss" scoped>

</style>