<template>
  <div>
    <h3>좋아하는 갬동님 LIST</h3>
    <LikeDirector />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '../../stores/counter';
import LikeDirector from '../../components/LikeDirector.vue';
import axios from 'axios';
const route = useRoute()
const store = useCounterStore()

const LikeDirectors = ref([])

</script>

<style scoped>

</style>