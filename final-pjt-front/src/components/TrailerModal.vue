<template>
  <div class="modal" v-if="showModal">
    <!-- YouTube 트레일러를 표시하기 위한 iframe을 여기에 추가하거나 다른 방법을 사용하세요 -->
    <iframe width="560" height="315" :src="getYouTubeUrl()" frameborder="0" allowfullscreen></iframe>
    <button @click="closeModal">닫기</button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const showModal = ref(false);
const movieId = ref(null);

const openModal = (id) => {
  movieId.value = id;
  showModal.value = true;
};

const closeModal = () => {
  movieId.value = null;
  showModal.value = false;
};

const getYouTubeUrl = computed(() => {
  // movieId를 기반으로 YouTube 트레일러 URL을 가져오는 로직을 구현하세요.
  // 예: return `https://www.youtube.com/embed/${movieId.value}`;
  return '';
});
</script>

<style scoped>
/* 모달 스타일을 여기에 추가하세요 */
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 20px;
  border: 1px solid #ccc;
}
</style>
