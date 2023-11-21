<template>
  <h1 class="neon-effect">dasuney+</h1>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  setup() {
    // ref를 사용하여 타이머 상태를 저장
    const timerFinished = ref(false)

    // onMounted 훅에서 타이머 설정
    onMounted(() => {
      setTimeout(() => {
        // 타이머가 끝나면 timerFinished 값을 true로 변경하고 라우터 이동
        timerFinished.value = true
      }, 3000)
    })

    return {
      timerFinished
    }
  },

  // watch를 사용하여 timerFinished 값이 변경될 때마다 라우터 이동
  watch: {
    timerFinished(value) {
      if (value) {
        this.$router.push('/intro')
      }
    }
  }
}


</script>

<style>
.neon-effect {
  font-family: disney;
  font-size: 200px;
  margin-top: 200px;
  text-align: center;
  color: #fff; /* Set initial text color */

  /* Animation for the neon effect */
  animation: neonGlow 1.5s ease-in-out infinite alternate;

  /* Add a shadow to simulate the neon glow */
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
}

@keyframes neonGlow {
  0% {
    color: #fff; /* White color for glow effect */
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
  }
  100% {
    color: rgb(17, 154, 239); /* Your desired neon color */
    text-shadow: 0 0 20px rgb(23, 108, 245), 0 0 30px rgb(24, 176, 246), 0 0 40px rgb(29, 135, 249); /* Add more glow layers */
  }
}
</style>