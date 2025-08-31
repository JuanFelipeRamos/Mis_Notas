<script setup>

defineProps({
  name: String
})

</script>


<template>
    <div class="container">
        <p>{{ name }}</p>
    </div>
</template>


<style scoped>
p {
  text-align: center;
  width: 170px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-left: 10px;
}

</style>