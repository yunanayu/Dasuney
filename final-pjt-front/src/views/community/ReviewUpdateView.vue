<template>
  <div>
    <h1>리뷰 작성 페이지</h1>
    <form @submit.prevent="UpdateReview">
      <label for="title">제목</label>
      <input type="text" id="title" v-model="title">
      <label for="content">내용</label>
      <textarea name="" id="content" cols="30" rows="10" v-model="content"></textarea>
      <input type="submit" value="리뷰 수정">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '../../stores/counter';

const store = useCounterStore()
const router = useRouter()
const route = useRoute()

const title = ref(route.query.reviewTitle)
const content = ref(route.query.reviewContent)

// console.log(route.query);
// console.log(route.query.reviewTitle);
// console.log(route.query.reviewContent);
const UpdateReview = function () {
  axios({
    method : 'put',
    url : `http://127.0.0.1:8000/community/reviews/${route.params.reviewid}/`,
    headers : {
        Authorization:`Token ${store.Token}`
      },
    data : {
      title : title.value,
      content : content.value
    }
  })
  .then((res) => {
    // console.log(res.data)
    window.alert('리뷰 수정이 완료되었습니다.')
    // title.value = ''
    // content.value = ''
    router.push({name:'moviedetail', params : {movieId:route.query.movieId}})
  })
  .catch(err => console.log(err))
}
</script>

<style lang="scss" scoped>

</style>