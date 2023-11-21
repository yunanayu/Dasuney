<template>
  <h1>dasney+</h1>
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

</style>