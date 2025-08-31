<script setup>
defineProps({
  txt: String
})

</script>


<template>
    <div>
        <button class="btn-grupo">{{ txt }}</button>
    </div>
</template>


<style scoped>
.btn-grupo {
  background-color: #c79f6e;
  color: black;
  padding: 12px;
  width: 100%;
  font-weight: bold;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-grupo:hover {
  background-color: #bb925f;
}

</style>