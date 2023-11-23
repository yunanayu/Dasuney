<!-- TrailerModal.vue -->
<template>
  <div class="modal" v-if="showModal">
    <iframe width="560" height="315" :src="youtubeVideoUrl" frameborder="0" allowfullscreen></iframe>
    <button @click="closeModal">닫기</button>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';
import { useCounterStore } from '../stores/counter';

const store = useCounterStore()

const showModal = ref(false);
const movieId = ref(null);
const youtubeVideoUrl = ref('');

const openModal = (id) => {
  movieId.value = id;
  showModal.value = true;
  searchYouTubeTrailer();
};

const closeModal = () => {
  movieId.value = null;
  showModal.value = false;
};

// const searchYouTubeTrailer = async () => {
//   try {
//     const response = await axios.get('https://www.googleapis.com/youtube/v3/search', {
//       params: {
//         q: `오피셜 트레일러 ${movieId.value}`,  // 필요에 따라 쿼리를 수정하세요
//         part: 'snippet',
//         type: 'video',
//         key: `${store.YOUTUBE_KEY}`,  // 여러분의 YouTube Data API 키로 교체하세요
//       },
//     });

//     if (response.data.items.length > 0) {
//       const videoId = response.data.items[0].id.videoId;
//       youtubeVideoUrl.value = `https://www.youtube.com/embed/${videoId}`;
//     }
//   } catch (error) {
//     console.error('YouTube 트레일러 검색 중 오류 발생:', error);
//   }
// };

const searchYouTubeTrailer = function () {
  axios({
    method :'GET',
    url : `https://www.googleapis.com/youtube/v3/search/?key=${store.YOUTUBE_KEY}&part=snippet&type=video&q=${movieId.value}`
  })
  .then((res) => {
    console.log(res.data);
  })
}


// movieId 변경 감지 및 YouTube 검색 트리거
watch(movieId, searchYouTubeTrailer);

// 선택적: 모달이 닫힐 때 (비디오 URL 지우기 등) 처리할 로직 추가
onMounted(() => {
  openModal

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
