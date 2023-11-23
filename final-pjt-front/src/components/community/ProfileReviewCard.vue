<template>
  <!-- <div class="container">
    <div class="chat-list">
      <div class="chat-base">
      </div>
    </div>
  </div> -->
  <div class="chat-item">
    <!-- {{ review.movie }} -->
    <div @click.prevent="goMoviewDetail(review.movie.movie_id)" >
      <img :src="review.movie.poster_path" alt="">
      <p>제목 : {{ review.movie.title }}</p>
    </div>
    <div  @click.prevent="goReviewDetail(review.id)" >
      <p class="chat-content">{{ review.content }}</p>
      <p>생성 시간 {{ review.created_at }}</p>
      <p>수정 시간 ㅋㅎ{{ review.updated_at }}</p>
    </div>
    <!-- <p class="chat-author" style="text-align: right;">{{ review.user.username }}</p> -->
    <hr class="chat-divider">
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

defineProps({
  review: Object,
});

const goReviewDetail = function (reviewId) {
  router.push({ name: 'reviewDetail', params: { reviewid: reviewId } });
};

const goMoviewDetail = function (movieId) {
  router.push({ name: 'moviedetail', params: { movieId: movieId } });
}
</script>

<style scoped>
.container {
  font-family: 'Arial', sans-serif;
  max-width: 800px;
  margin: 0 auto;
  
}

.chat-list {
  padding: 20px;
  width: 400px;
  position: relative;
}

.chat-item {
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.chat-item:hover {
  background-color: #f5f5f5;
}

.chat-content {
  margin-bottom: 5px;
}

.chat-author {
  font-style: italic;
  color: #888;
}

.chat-divider {
  margin-top: 10px;
  border: 1px solid #ddd;
}
.chat-base {

}
</style>
