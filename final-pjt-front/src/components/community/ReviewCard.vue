<template>
  <div class="container">
    <div class="chat-list">
      <div class="chat-base">
        <div @click.prevent="goReviewDetail(review.id)" class="chat-item">
          <div class="content-container">
            <p class="chat-content clamp-lines">{{ review.content }}</p>
          </div>
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
.clamp-lines {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
    -webkit-line-clamp: 3; /* 필요에 따라 줄 수를 조정하세요. */
  }

  .content-container {
    max-height: calc(3 * 1.6em); /* 1.2em은 줄 높이입니다. */
    overflow: hidden;
  }
</style>
