<template>
  <div v-if="follows" class="follow-list">
    <div v-for="follow in follows" :key="follow.id" class="follow-item">
      <span @click="goProfile(follow.username)">{{ follow.username }}</span>
    </div>
    <button @click="closeFollow" class="close-button">닫기</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

defineProps({
  follows: Array,
});

const emit = defineEmits(['closeFollow']);

const closeFollow = function () {
  emit('closeFollow');
};

const goProfile = function (username) {
  router.push({ name: 'profile', params: { username: username } });
};
</script>

<style lang="scss" scoped>
.follow-list {
  /* 전체 목록 스타일 */
  margin-top: 10px;
}

.follow-item {
  /* 개별 팔로우 아이템 스타일 */
  margin-bottom: 5px;
  font-size: 20px;
  text-align: center;
  // border: 1px solid ;
}
.follow-item:hover {
  background-color: #2980b9;
}

span {
  /* 팔로우 유저명 스타일 */
  cursor: pointer;
  color: #4caf50; /* 디즈니 테마와 일치하는 녹색 */
  font-weight: bold;
  margin-right: 10px;
  transition: color 0.3s;
}

span:hover {
  /* 마우스 오버 시 스타일 */
  color: #45a049; /* 마우스 오버 시 더 어두운 녹색 */
}

.close-button {
  /* 닫기 버튼 스타일 */
  cursor: pointer;
  color: gainsboro;
  font-weight: bold;
  margin-top: 10px;
  transition: color 0.3s;
  background-color: #ff4081;
  
}

.close-button:hover {
  /* 마우스 오버 시 스타일 */
  color: #d81b60; /* 마우스 오버 시 더 어두운 분홍색 */
}
</style>
