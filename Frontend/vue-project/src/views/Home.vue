<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/axios'
import ModalCrearAlgo from '@/components/ModalCrearAlgo.vue'
import TxtGrupoList from '@/components/TxtGrupoList.vue'

const isLoggedIn = ref(true)
const router = useRouter()

// cerrar sesión
function logout() {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
  isLoggedIn.value = false
  router.push('/')
  console.log('Sesión cerrada con éxito')
}

// ver si el usuario no tiene token de acceso para la ruta de este componente
let token = localStorage.getItem('access')
if (!token) {
  router.push('/msgsinacceso')
}

const showModal = ref(false)

// listar grupos
const grupo = ref([])

const listarGrupos = async () => {
  try {
    const response = await api.get('/tareas/listar_grupos/',
      {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    grupo.value = response.data

    if (grupo.value.length === 0) {
      console.log("No hay registros de grupos")
    } else {
      console.log("Sí hay registros de grupos")
    }
  } catch (error) {
    console.error(error)
  }
}

onMounted(() => {
  listarGrupos()
})

</script>


<template>
  <div class="home-container">
    <ModalCrearAlgo v-model="showModal" h1="INGRESA UN TÍTULO" txtButton="Crear grupo" />
    <div class="grupos">
      <div class="contenido-grupo">
        <h2>GRUPOS</h2>
        <hr />
        <button @click="showModal = true" class="btn-grupo">Añadir grupo</button>
      </div>

      <div class="cerrar-sesion">
        <hr />
        <a @click.prevent="logout">Cerrar sesión</a>
      </div>
    </div>

    <div class="listas">
      <h2>TUS LISTAS</h2>
      <hr />
      <p v-if="grupo.length === 0" class="no-listas">
        Aún no tienes ninguna lista
      </p>

      <div v-else>
        <TxtGrupoList v-for="g in grupo" :key="g.id" :name="g.name" />
      </div>
    </div>
  </div>
</template>


<style scoped>
.home-container {
  display: flex;
  height: 100vh;
  font-family: sans-serif;
}

.grupos {
  width: 260px;
  background-color: #b67e3d;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px;
  box-sizing: border-box;
}

.contenido-grupo h2 {
  margin-bottom: 10px;
  font-size: 24px;
  font-weight: bold;
  color: #000;
}

.contenido-grupo hr {
  border: 0.5px solid #000;
  margin-bottom: 30px;
}

.btn-grupo {
  background-color: #c79f6e;
  color: #fff;
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

.cerrar-sesion {
  text-align: center;
}

.cerrar-sesion hr {
  border: 0.5px solid #000;
  margin-bottom: 15px;
}

.cerrar-sesion a {
  margin: 0;
  font-weight: bold;
  cursor: pointer;
  color: #000;
  text-decoration: none;
}

.cerrar-sesion a:hover {
  color: white;
}

.listas {
  flex: 1;
  background-color: #320f0c;
  padding: 30px;
  color: #fff;
  box-sizing: border-box;
}

.listas h2 {
  text-align: center;
  font-size: 26px;
  font-weight: bold;
  margin-bottom: 20px;
}

.listas hr {
  border: 0.5px solid #ccc;
  margin-bottom: 20px;
}

.no-listas {
  font-size: 18px;
  text-align: center;
  margin-top: 25px;
}
</style>
