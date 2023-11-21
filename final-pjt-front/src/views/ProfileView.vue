<template>
  <div>
    <h1>프로필 페이지 ㅋㅎㅋㅎ</h1>
    <div class="myprofile">
      <img src="data:image/png;base64,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" alt="" style="width: 200px;">
    </div>
    <button @click="follow" v-show="followbutton">{{ isFollowing ? '언팔로우' : '팔로우' }}</button>
    <div class="follow-count">
      <p>팔로우: {{ followings.length }}</p>
      <p>팔로워: {{ followers.length }}</p>
    </div>
    <div class="category">
      <nav>
        <RouterLink to="/starrating">평가 ({{ ratingCount }})</RouterLink> |
        <RouterLink :to="{name:'actorlike', params:{username:route.params.username}}">배우b ({{ LikeActors.length }})</RouterLink> |
        <RouterLink to="/directorlike">감독b ({{ LikeDirectors.length }})</RouterLink> |
        <RouterLink to="/hopemovie">보고싶어요 ({{ HopeMovies.length }})</RouterLink>
      </nav>
    </div>
  </div>
  <RouterView />
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted, computed } from 'vue';
import { RouterLink, RouterView } from 'vue-router';
import { useCounterStore } from '../stores/counter';
import { useRoute } from 'vue-router';
const route = useRoute()
const store = useCounterStore()

// 팔로우 기능 

const followers = ref([])
const followings = ref([])

const followbutton = computed(() => {
  if (store.tempUsername === route.params.username) {
    return false
  } else {
    return true
  }
})

const isFollowing = computed(() => {
  return followers.value.some(follower => follower.username === store.tempUsername);
})

const follow = function () {
  axios({
    method : 'post',
    url : `http://127.0.0.1:8000/accounts/profile/${route.params.username}/`,
    headers : {
        Authorization:`Token ${store.Token}`
      }
  })
  .then((res) => {
    // console.log(res)
    if (res.data.is_followed === true) {
      followers.value.push(
        { id : res.data.userId,
          username : store.tempUsername
        }
      )
    } else {
      const index = followers.value.findIndex((follow) => follow.username === store.tempUsername)
      followers.value.splice(index, 1)
    }
    // console.log(followers.value)
  })
  .catch(err=>console.log(err))
}
// 영화 감독 배우 조하여
const LikeActors = ref([])
const HopeMovies = ref([])
const LikeDirectors = ref([])

const ratingCount = ref(0);

onMounted(() => {
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/accounts/profile/${route.params.username}/`,
    headers : {
        Authorization:`Token ${store.Token}`
      }
  })
  .then((res) => {
    // console.log(res);
    followers.value = res.data.followers
    followings.value = res.data.followings
    LikeActors.value = res.data.like_actor
    LikeDirectors.value = res.data.like_director
    HopeMovies.value = res.data.like_movies
    // console.log(LikeActors.value);
  })
  .catch(err=>console.log(err))
  // store.getActors()
  // console.log(store.actors)
});
</script>

<style scoped>
.myprofile {
  border: solid 1px black;
  width: 350px;
  height: 300px;
  text-align: center;
  margin-bottom: 10px;
}

.follow-count {
  border: solid 1px black;
  width: 350px;
  text-align: center;
}

.category {
  border: solid 1px black;
  width: 350px;
  height: 30px;
  text-align: center;
}
</style>
