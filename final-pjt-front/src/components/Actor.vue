<template>
  <div>
    <p>{{ cast.name }}</p>
    <p>{{ cast.id }}</p>
    <button>좋아여</button>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
defineProps({
  cast:Object
})

</script>

<style scoped>

</style>