<template>
  <div class="container">
    <div class="review-list">
      <div @click.prevent="goReviewDetail(review.id)">
        <!-- {{  review }} -->
        <!-- <p>리뷰 타이틀 : {{ review.title }}</p> -->
        <p>리뷰 내용 : {{ review.content }}</p>
        <p>리뷰 작성자 ; {{  review.user.username }}</p>
        <hr>

        <!-- <h1>고 리뷰 디테일</h1>
          <p>리뷰 수정 버튼</p>
          <p>리뷰 </p> -->
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
// import router from '../../router';

const router = useRouter()

defineProps({
  review : Object
})


const goReviewDetail = function (reviewId) {
  router.push({name:'reviewDetail', params:{reviewid:reviewId}})   
}


</script>

<style scoped>
.review-list {
  font-family: 'Arial', sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
</style>