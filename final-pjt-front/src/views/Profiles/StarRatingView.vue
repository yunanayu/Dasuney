<template>
  <div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import LikeActor from '@/components/LikeActor.vue'
import Actor from '../../components/Actor.vue';
import { useCounterStore } from '../../stores/counter';
import axios from 'axios';
const route = useRoute()
const store = useCounterStore()

console.log(route.params)
</script>

<style scoped>

</style>
