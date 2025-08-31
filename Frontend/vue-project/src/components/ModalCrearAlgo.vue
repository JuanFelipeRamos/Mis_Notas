<script setup>
import api from '../services/axios'
import { ref } from 'vue'

defineProps({
  modelValue: Boolean,
  h1: String,
  txtButton: String
})

function closeModal() {
  emit("update:modelValue", false)
}

const emit = defineEmits(["update:modelValue", "grupoCreado"])

// Crear grupo
const token = localStorage.getItem("token")
const grupo = ref({
  name: ''
})

const crearGrupo = async () => {
  try {
    if (grupo.value.name.length > 32) {
      alert("Debes ingresar un título más corto")
      return
    }

    const response = await api.post('/tareas/crear_grupo/', {
      name: grupo.value.name
    }, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    grupo.value = {
      name: ''
    }

    emit("update:modelValue", false)
    emit('grupoCreado')

    alert("Grupo creado exitosamente")
  } catch (error) {
    alert("Error al crear grupo")
    console.error(error)

    grupo.value = {
      name: ''
    }
  }
}

</script>

<template>
  <div class="modal-container" v-if="modelValue" @click.self="closeModal">
    <div class="modal-box">
      <h1>{{ h1 }}</h1>
      <form @submit.prevent="crearGrupo">
        <input type="text" placeholder="ESCRIBE AQUÍ..." v-model="grupo.name" required />
        <button>{{ txtButton }}</button>
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
