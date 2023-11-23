<template>
  <div v-if="follows">
    <div v-for="follow in follows">
      <span @click="goProfile(follow.username)">{{ follow.username }}</span>
    </div>
    <span @click="closeFollow">닫기</span>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()

defineProps({
  follows : Array
})

const emit = defineEmits(['closeFollow'])
const closeFollow = function () {
  emit('closeFollow')
}

const goProfile = function (username) {
  router.push({name:'profile', params:{username:username}})
}
</script>

<style lang="scss" scoped>

</style>