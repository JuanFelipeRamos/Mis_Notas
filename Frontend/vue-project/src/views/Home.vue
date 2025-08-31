<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/axios'
import ModalCrearGrupo from '@/components/ModalCrearGrupo.vue'
import TxtGrupoList from '@/components/TxtGrupoList.vue'
import ButtonComponent from '@/components/ButtonComponent.vue'

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
const cantGrups = ref(0)

const listarGrupos = async () => {
  try {
    const response = await api.get('/tareas/listar_grupos/',
      {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    grupo.value = response.data
    console.log(grupo.value)

    if (grupo.value.length === 0) {
      console.log("No hay registros de grupos")
    } else {
      console.log("Sí hay registros de grupos")
    }

    cantGrups.value = grupo.value.length
  } catch (error) {
    console.error(error)
  }
}

onMounted(() => {
  listarGrupos()
})

// mostrar nombre del grupo en el tablero al dar click en grupo
const nameSelecionado = ref('')
const idGrupo = ref()
const nameEnMayusculas = ref('')
const seHaSeleccionado = ref(false)

function verGrupo(grupo) {
  idGrupo.value = grupo.id
  nameSelecionado.value = grupo.name
  nameEnMayusculas.value = nameSelecionado.value.toUpperCase()

  if (nameSelecionado.value == '') {
    console.log("No se ha seleccionado un grupo para visualizarlo")
  } else {
    seHaSeleccionado.value = true
  }
}

</script>


<template>
  <div class="home-container">
    <ModalCrearGrupo v-model="showModal" @grupoCreado="listarGrupos" />
    <div class="grupos">
      <div class="contenido-grupo">
        <div class="txtGrupoYCantidad">
          <h2>GRUPOS -</h2>
          <h2 class="h2ConEspacio">{{ cantGrups }}</h2>
        </div>
        <hr />
        <ButtonComponent @click="showModal = true" txt="Añadir Grupo" />
        <div v-if="grupo.length > 0">
          <TxtGrupoList v-for="g in grupo" :key="g.id" :name="g.name" :value="g.id" @click="verGrupo(g)" class="listGrups" />
        </div>
      </div>

      <div class="cerrar-sesion">
        <hr />
        <a @click.prevent="logout">Cerrar sesión</a>
      </div>
    </div>

    <div class="listas">
      <div class="txtNameGrupo">
        <h2>TUS LISTAS</h2>
        <h2 v-if="seHaSeleccionado" class="h2ConEspacio">DE {{ nameEnMayusculas }}</h2>
      </div>
      <hr />
      <p v-if="grupo.length === 0" class="no-listas">
        Aún no tienes ningun grupo, crea uno para empezar a crear listas y tareas.
      </p>
      <p v-if="grupo.length > 0 && !seHaSeleccionado" class="no-listas">
        Elije un grupo para ver sus listas y tareas.
      </p>

      <ButtonComponent v-if="seHaSeleccionado" txt="Añadir lista" class="btnAddLista" />
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

.listGrups {
  background-color: #c79f6e;
  color: white;
  padding: 12px;
  font-weight: bold;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.listGrups:hover {
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
  padding: 20px;
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

.listGrups {
  margin-top: 7px;
}

.txtGrupoYCantidad, .txtNameGrupo {
  display: flex;
  justify-content: center;
}

.h2ConEspacio {
  margin-left: 6px;
}

.btnAddLista {
  width: 310px;
}

</style>
