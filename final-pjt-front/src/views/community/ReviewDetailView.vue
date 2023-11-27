<template>
  <div class="review-detail" v-if="review.user">
    <div class="header">
      <h3>{{ review.title }}</h3>
      <div class="metadata">
        <p>{{ review.user.username }}</p>
        <p>{{ review.created_at }}</p>
        <!-- <p> 수정일 : {{ review.updated_at }} </p> -->
      </div>
    </div>
    <div class="content">
      <hr>
      <p>{{ review.content }}</p> 
      <hr>
      <div class="actions">
        <button @click.prevent="goUpdate" class="action-button" style="margin-right: 10px;" v-show="review.user.username == store.tempUsername">수정</button>
        <button @click.prevent="goDelete" class="action-button danger" v-show="review.user.username == store.tempUsername">삭제</button>
      </div>
    </div>
    <div class="comments-section">
      <form @submit.prevent="createComment" class="comment-form">
        <input type="text" v-model="commentContent" placeholder="댓글을 입력하세요">
        <button type="submit" class="action-button">댓글 작성</button>
      </form>
      <div class="comment-list" v-if="commentList">
        <div v-for="comment in commentList" :key="comment.id" class="comment">
          <span>{{ comment.content }}</span>
          <div class="comment-metadata">
            <span>작성자: {{ comment.user.username }}</span> 
            <button @click.prevent="deleteComment(comment.id)" class="action-button danger" v-show="comment.user.username == store.tempUsername">댓글 삭제</button>
          </div>
          <hr>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute,useRouter } from 'vue-router';
import axios from 'axios';
import { useCounterStore } from '../../stores/counter';
const store = useCounterStore()
const route = useRoute()
const router  = useRouter()
// console.log(route.params.reviewid)

const commentContent = ref('')
const commentList = ref([])
const review = ref({})
onMounted(() => {
  // 리뷰 디테일 요청
  axios({
      method : 'get',
      url : `http://127.0.0.1:8000/community/reviews/${route.params.reviewid}/`,
      headers: {
          Authorization: `Token ${store.Token}`
        },
    })
    .then((res)=>{
      // console.log(res.data);
      review.value = res.data
    })
    .catch((err)=>console.log(err))
  
  // 리뷰 댓글 목록 요청
  axios({
      method : 'get',
      url : `http://127.0.0.1:8000/community/reviews/${route.params.reviewid}/comments/`,
      headers: {
          Authorization: `Token ${store.Token}`
        },
    })
    .then((res)=>{
      // console.log(res.data);
      commentList.value = res.data
    })
    .catch((err)=>console.log(err))
  
})

const goDelete = function () {
  axios({
    method : 'DELETE',
    url : `http://127.0.0.1:8000/community/reviews/${route.params.reviewid}/`,
    headers: {
      Authorization: `Token ${store.Token}`
    },
    })
    .then((res)=>{
      // console.log(res.data);
      window.alert('삭제 완료')
      router.push({name:'moviedetail', params:{movieId:review.value.movie.movie_id}})

    })
    .catch((err)=>console.log(err))
}

const goUpdate = function () {
  router.push({name:'reviewupdate', params:{reviewid :route.params.reviewid}, query:{reviewTitle:review.value.title, reviewContent:review.value.content, movieId:review.value.movie.movie_id}})
}

// 댓글 작성
const createComment = function () {
  axios({
    method : 'post',
    url : `http://127.0.0.1:8000/community/reviews/${route.params.reviewid}/comments/`,
    headers: {
      Authorization: `Token ${store.Token}`
    },
    data : {
      content : commentContent.value
    } 
  })
  .then((res) => {
    // console.log(res.data);
    commentList.value.push(res.data)
    commentContent.value = ''
  })
  .catch(err => console.log(err))
}

// 댓글 삭제
const deleteComment = function (commentId) {
  axios({
    method : 'delete',
    url : `http://127.0.0.1:8000/community/comments/${commentId}/`,
    headers: {
      Authorization: `Token ${store.Token}`
    },
  })
  .then((res) => {
    window.alert('댓글 삭제 완료!')
    const index = commentList.value.findIndex((comment) => comment.id == commentId)
    commentList.value.splice(index, 1)
  })
  .catch(err => console.log(err))
}
</script>

<style scoped>
.review-detail {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  color: #0b1f35;
}

.header {
  /* display: flex; */
  /* justify-content: space-between; */
  align-items: center;
}

.metadata {
  color: #8b8989;
}

.content {
  margin-top: 20px;
}

.actions {
  /* display: flex;
  justify-content: space-between; */
  margin-top: 20px;
  margin-bottom: 100px;
}

.action-button {
  padding: 10px;
  cursor: pointer;
  background-color: #3498db;
  color: #fff;
  border: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.action-button:hover {
  background-color: #2980b9;
}

.danger {
  background-color: #e74c3c;
}

.comment-list {
  margin-top: 20px;
}

.comment {
  margin-bottom: 10px;
}

.comment-metadata {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #777;
}

.comment-form {
  display: flex;
  align-items: center;
  margin-top: 20px;
}

.comment-form input {
  padding: 10px;
  flex: 1;
  margin-right: 10px;
}

.comment-form button {
  padding: 10px;
  cursor: pointer;
  background-color: #3498db;
  color: #fff;
  border: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.comment-form button:hover {
  background-color: #2980b9;
}
</style>