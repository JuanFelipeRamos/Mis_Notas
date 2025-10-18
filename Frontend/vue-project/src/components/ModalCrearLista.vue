<script setup>
import { ref } from 'vue'
import api from '../services/axios'

const props = defineProps({
  modelValue: Boolean,
  dato: Number
})

const emit = defineEmits(["update:modelValue", "listaCreada"])

function closeModal() {
  emit("update:modelValue", false)
}

// Crear lista
const token = localStorage.getItem("token")
const lista = ref({
  name: '',
  description: ''
})

const crearLista = async () => {
  try {
    if (lista.value.name.length > 41) {
      alert("Debes ingresar un nombre más corto")
      return
    }

    if (lista.value.description.length > 100) {
      alert("Debes ingresar una descripción más corta")
      return
    }

    const response = await api.post('/tareas/listas/', {
      name: lista.value.name,
      description: lista.value.description,
      id_grupo: props.dato
    }, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    lista.value = {
      name: '',
      description: ''
    }

    emit("update:modelValue", false)
    emit('listaCreada')

    alert("Lista creada exitosamente")
  } catch (error) {
    alert("Error al crear lista")
    console.error(error)

    lista.value = {
      name: '',
      description: ''
    }
  }
}

</script>

<template>
  <div class="modal-container" v-if="modelValue" @click.self="closeModal">
    <div class="modal-box">
      <h1>AÑADE UNA LISTA</h1>
      <form @submit.prevent="crearLista">
        <input type="text" placeholder="NOMBRE" v-model="lista.name" required />
        <input type="text" placeholder="DESCRIPCIÓN (OPCIONAL)" v-model="lista.description" />
        <button>Crear lista</button>
      </form>
      <a @click.prevent="closeModal">Cancelar</a>
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

.modal-box button {
  background-color: #5d0000;
  color: white;
  border: none;
  padding: 12px;
  width: 100%;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  margin: 20px 0px;
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
</style>
