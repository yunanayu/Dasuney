<template>
  <div class="chat-container">
    <div class="chat-header">
      <h1>리뷰 작성 페이지</h1>
    </div>
    <div class="chat-body">
      <div class="message">
        <p><strong>Bot:</strong> 안녕하세요! 리뷰를 작성해보세요.</p>
      </div>
      <form @submit.prevent="createReview" class="message">
        <div class="input-group">
          <label for="title">제목</label>
          <input type="text" id="title" v-model="title">
        </div>
        <div class="input-group">
          <label for="content">내용</label>
          <textarea id="content" v-model="content" cols="30" rows="3"></textarea>
        </div>
        <button type="submit">리뷰 작성</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { routeLocationKey, useRoute } from 'vue-router'
import { useCounterStore } from '../../stores/counter';
import router from '../../router';
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
  .then((res) => {
    console.log(res.data)
    window.alert('리뷰 작성이 완료되었습니다.')
    title.value = ''
    content.value = ''
    router.push({name:'moviedetail', params : {movieId:route.query.movie_id}})
  })
  .catch(err => console.log(err))
}
</script>

<style scoped>
.chat-container {
  max-width: 400px;
  margin: 20px auto;
  border: 1px solid #ccc;
  border-radius: 10px;
  overflow: hidden;
}

.chat-header {
  background-color: #4CAF50;
  color: white;
  padding: 10px;
  text-align: center;
}

.chat-body {
  padding: 20px;
}

.message {
  background-color: #f1f1f1;
  border-radius: 5px;
  margin-bottom: 10px;
  padding: 10px;
}

.input-group {
  margin-bottom: 10px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input, textarea {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  margin-bottom: 10px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #45a049;
}
</style>