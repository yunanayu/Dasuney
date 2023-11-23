<template>
  <div class="update-review-container">
    <h1>리뷰 수정 페이지</h1>
    <form @submit.prevent="UpdateReview" class="review-form">
      <label for="title">제목</label>
      <input type="text" id="title" v-model="title">
      <label for="content">내용</label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
      <input type="submit" value="리뷰 수정" class="submit-button">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '../../stores/counter';

const store = useCounterStore();
const router = useRouter();
const route = useRoute();

const title = ref(route.query.reviewTitle);
const content = ref(route.query.reviewContent);

const UpdateReview = function () {
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/community/reviews/${route.params.reviewid}/`,
    headers: {
      Authorization: `Token ${store.Token}`
    },
    data: {
      title: title.value,
      content: content.value
    }
  })
    .then((res) => {
      window.alert('리뷰 수정이 완료되었습니다.');
      router.push({ name: 'moviedetail', params: { movieId: route.query.movieId } });
    })
    .catch(err => console.log(err));
};
</script>

<style lang="scss" scoped>
.update-review-container {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  background-color: #fff;
  color: rgb(54, 45, 123);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

h1 {
  text-align: center;
}

.review-form {
  margin-top: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input,
textarea {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
  margin-bottom: 15px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.submit-button {
  background-color: #4CAF50;
  color: white;
  padding: 12px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #45a049;
}
</style>
