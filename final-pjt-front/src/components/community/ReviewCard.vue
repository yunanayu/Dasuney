<template>
  <div class="container">
    <div class="chat-list">
      <div class="chat-base">
      <div @click.prevent="goReviewDetail(review.id)" class="chat-item">
        <p class="chat-content">{{ review.content }}</p>
        <p class="chat-author" style="text-align: right;">{{ review.user.username }}</p>
        <hr class="chat-divider">
        </div>
      </div>
    </div>
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
</script>

<style scoped>
.container {
  font-family: 'Arial', sans-serif;
  max-width: 800px;
  margin: 0 auto;
  
}

.chat-list {
  padding: 20px;
  width: 300px;
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
  border: 1px solid black;
}
</style>
