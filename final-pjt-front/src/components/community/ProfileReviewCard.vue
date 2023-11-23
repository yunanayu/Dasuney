<template>
<div class="chat-item">
  <div class="image-container" @click.prevent="goMoviewDetail(review.movie.movie_id)">
    <img :src="review.movie.poster_path" alt="">
  </div>
  <div class="text-container" @click.prevent="goReviewDetail(review.id)">
    <p class="title">제목: {{ review.movie.title }}</p>
    <p class="chat-content">{{ review.content }}</p>
  </div>
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
.chat-item {
  display: flex;
  align-items: center;
  margin-bottom: 20px; /* Adjust margin as needed */
}

.image-container {
  cursor: pointer;
  margin-right: 20px; /* Adjust margin as needed */
}

.image-container img {
  width: 150px; /* Adjust width as needed */
  height: auto;
}

.text-container {
  flex: 1;
}

.title {
  font-weight: bold;
  margin-bottom: 5px; /* Adjust margin as needed */
}

.chat-content {
  margin: 0;
}

.chat-divider {
  margin-top: 20px; 
}
.chat-item:hover {
  background-color: #484545;
}
/* .chat-list {
  padding: 20px;
  width: 400px;
  position: relative;
}

.chat-item {
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.chat-item img {
  width: 200px;
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
} */

</style>
