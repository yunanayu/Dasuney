<template>
  <div v-if="director">
    <p>{{ director.name }}</p>
    <p>{{ director.id }}</p>
  </div>
</template>

<script setup>
defineProps({
  director:Object
})
</script>

<style scoped>

</style>