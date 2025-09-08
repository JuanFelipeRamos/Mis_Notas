<script setup>
const props = defineProps({
  modelValue: Boolean,
  description: String
})

const emit = defineEmits(["update:modelValue"])

function closeModal() {
  emit("update:modelValue", false)
}
</script>

<template>
  <div class="modal-container" v-if="modelValue" @click.self="closeModal">
    <div class="modal-box">
      <h1>DESCRIPCIÓN DE ESTE GRUPO</h1>
      <p>{{ description }}</p>
      <a @click.prevent="closeModal">Salir</a>
    </div>
  </div>
</template>


<style scoped>
.modal-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: rgba(14, 0, 0, 0.7);
  backdrop-filter: blur(3px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.modal-box {
  background-color: #c3863f;
  padding: 55px 40px;
  text-align: center;
  border-radius: 12px;
  width: 400px;
  position: relative;
}

.modal-box h1 {
  font-size: 24px;
  margin-bottom: 30px;
  font-weight: bold;
  color: #000;
}

.modal-box input {
  display: block;
  width: 100%;
  padding: 12px;
  margin: 10px 0;
  border-radius: 8px;
  border: none;
  font-size: 14px;
}

.modal-box a {
  margin-top: 25px;
  font-size: 16px;
  color: #000;
  text-decoration: none;
  cursor: pointer;
}

.modal-box a:hover {
  color: white;
}

p {
  color: black;
  margin-bottom: 30px;
  font-style: italic;
}
</style>
