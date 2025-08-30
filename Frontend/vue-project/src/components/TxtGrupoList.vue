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
}

</style>