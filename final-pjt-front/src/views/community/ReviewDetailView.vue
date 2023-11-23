<template>
  <div v-if="review.user">
    <h1>리뷰 디테일 페이지이고 여기서 수정 삭제를 다 할거랍니다? 그리도 댓글도 달 수 있어요ㅕ. 우와!!</h1>
    <!-- {{ review }} -->
    <h3>{{ review.title }}</h3>
    <hr>
    <p>작성자 : {{ review.user.username }}</p>
    <p>작성일 : {{ review.created_at }}</p>
    <p>수정일 : {{ review.updated_at }}</p>
    <hr>
    <span>{{ review.content }}</span> 
    <hr>
    <button @click.prevent="goUpdate">수정</button>
    <button @click.prevent="goDelete">삭제</button>
    <hr>
    <h1>댓글 목록</h1>
    <hr>
    <div v-if="commentList">
      <div v-for="comment in commentList">
        <!-- <p>{{ comment }}</p> -->
        <span>{{ comment.content }}</span>
        <br>
        <span>작성자 : {{ comment.user.username }}</span> 
        <button @click.prevent="deleteComment(comment.id)">댓글 삭제</button>
        <hr>
      </div>
    </div>
    <h1>댓글 작성</h1>
    <form @submit.prevent="createComment">
      <input type="text" v-model="commentContent">
      <input type="submit" value="댓글 작성">
    </form>
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
    console.log(res.data);
    commentList.value.push(res.data)
    commentContent.value = ''
  })
  .catch(err => console.log(err))
}

// 댓글 삭제
const deleteComment = function (commentId) {
  axios({
    method : 'delete',
    url : `http://127.0.0.1:8000/community/reviews/${route.params.reviewid}/comments/`,
    headers: {
      Authorization: `Token ${store.Token}`
    },
    data : {
      content : commentContent.value
    } 
  })
  .then((res) => {
    console.log(res.data);
  })
  .catch(err => console.log(err))
}
</script>

<style lang="scss" scoped>

</style>