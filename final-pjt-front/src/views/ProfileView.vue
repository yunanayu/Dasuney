<template>
  <div class="profile">
    <h1>Profile</h1>
    <div class="myprofile">
      <label for="profile-picture" class="profile-picture-label">
        <input
          type="file"
          id="profile-picture"
          accept="image/*"
          @change="handleProfilePictureChange"
          style="display: none"
        />
        <img
          v-if="profilePicture"
          :src="profilePicture"
          alt="프로필 사진"
          class="profile-picture"
        />
        <span v-else>프로필 사진 선택</span>
      </label>
    </div>
    <button @click="follow" v-show="followbutton">{{ isFollowing ? '언팔로우' : '팔로우' }}</button>
    <div class="follow-count">
      <p>팔로우: {{ followings.length }}</p>
      <p>팔로워: {{ followers.length }}</p>
    </div>
    <div class="category">
      <nav>
        <RouterLink to="/starrating">내 평가 ({{ ratingCount }})</RouterLink>
        <RouterLink :to="{name:'actorlike', params:{username:route.params.username}}">좋아하는 배우 ({{ LikeActors.length }})</RouterLink>
        <RouterLink to="/directorlike">좋아하는 감독 ({{ LikeDirectors.length }})</RouterLink>
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
const profilePicture = ref('');

// 프로필 사진 선택
const handleProfilePictureChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      profilePicture.value = e.target.result;
    };
    reader.readAsDataURL(file);
  }
};
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
.profile {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

h1 {
  font-size: 32px;
  margin-bottom: 20px;
}

.myprofile {
  /* background-color: #f5f5f5; */
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  margin-bottom: 20px;
}

.myprofile img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
}

button {
  margin-top: 10px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  background-color: #4caf50;
  color: #fff;
  border: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #45a049;
}

.follow-count p {
  font-size: 18px;
  margin: 5px 0;
}

.category nav {
  margin-top: 20px;
  text-align: center;
}

.category nav a {
  margin: 0 20px;
  text-decoration: none;
  color: #333;
  font-size: 18px;
  font-weight: bold;
  transition: color 0.3s;
}

.category nav a:hover {
  color: #4caf50;
}

.profile-picture-label {
  cursor: pointer;
  display: inline-block;
}

.profile-picture {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
  border: 2px solid #4caf50; /* 이미지가 선택된 경우의 테두리 색상 */
}

.profile-picture-label span {
  display: inline-block;
  padding: 10px;
  background-color: #4caf50; /* 이미지가 선택되지 않은 경우의 배경색상 */
  color: #fff;
  border-radius: 4px;
  cursor: pointer;
}
</style>
