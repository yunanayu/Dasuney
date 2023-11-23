<template>
  <div>
    <h1>리뷰 작성 페이지</h1>
    <form @submit.prevent="createReview">
      <label for="title">제목</label>
      <input type="text" id="title" v-model="title">
      <label for="content">내용</label>
      <textarea name="" id="content" cols="30" rows="10" v-model="content"></textarea>
      <input type="submit" value="리뷰 작성">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRoute } from 'vue-router'
import { useCounterStore } from '../../stores/counter';
const content = ref('')
const store = useCounterStore()
const title = ref('')
const route = useRoute()
const createReview = function () {
  axios({
    method : 'post',
    url : `http://127.0.0.1:8000/community/reviews/movie/${route.params.movieid}/`,
    headers : {
        Authorization:`Token ${store.Token}`
      },
    data : {
      title : title.value,
      content : content.value
    }
  })
}
</script>

<style lang="scss" scoped>

</style>