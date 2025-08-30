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
.container {
    background-color: #c79f6e;
    color: black;
    padding: 12px;
    width: 100%;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.container:hover {
  background-color: #bb925f;
}

</style>