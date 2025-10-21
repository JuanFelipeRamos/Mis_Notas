<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { listarGrupos, listarCantidadGrupos } from '@/services/grupos'
import { listarListasDeUnGrupo } from '@/services/listas'
import ModalCrearGrupo from '@/components/ModalCrearGrupo.vue'
import ModalCrearLista from '@/components/ModalCrearLista.vue'
import TxtGrupoList from '@/components/TxtGrupoList.vue'
import ButtonComponent from '@/components/ButtonComponent.vue'
import ModalCrearDescripcionGrupo from '@/components/ModalCrearDescripcionGrupo.vue'
import VerDescription from '@/components/VerDescription.vue'
import ModalBorrarGrupo from '@/components/ModalBorrarGrupo.vue'
import ListaComponent from '@/components/ListaComponent.vue'

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
const listaDeGrupos = ref([])
const cantidadDeGrupos = ref(0)
onMounted(async () => {
  try {
    listaDeGrupos.value = await listarGrupos();

    cantidadDeGrupos.value = await listarCantidadGrupos();
  } catch (error) {
    console.error('Error al cargar datos:', error);
  }
});


// mostrar nombre del grupo en el tablero al dar click en grupo
const nameSelecionado = ref('')
const idGrupo = ref()
const idLista = ref()
const nameEnMayusculas = ref('')
const descriptionSeleccionado = ref('')
const seHaSeleccionado = ref(false)
const listaDeListas = ref([])

function verGrupo(grupo, lista) {
  idGrupo.value = grupo.id
  nameSelecionado.value = grupo.name // capturar el name del grupo seleccionado
  nameEnMayusculas.value = nameSelecionado.value.toUpperCase()

  descriptionSeleccionado.value = grupo.description // capturar la descripción del grupo seleccionado
  
  if (nameSelecionado.value == '') {
    console.log("No se ha seleccionado un grupo para visualizarlo")
  } else {
    seHaSeleccionado.value = true
  }

  // mostrar listas del grupo seleccionado
  const verListas = async () => {
    try {
    listaDeListas.value = await listarListasDeUnGrupo(idGrupo.value);
    console.log("Listas de este grupo:\n", listaDeListas.value)
  } catch (error) {
    console.error('Error al cargar datos:', error);
  }
  }

  verListas()

  idLista.value = lista.id
}

// listar grupos actualizados
const actualizarGrupos = async () => {
  listaDeGrupos.value = await listarGrupos()
  cantidadDeGrupos.value = listaDeGrupos.value.length

  if (!listaDeGrupos.value.some(g => g.id === idGrupo.value)) {
    seHaSeleccionado.value = false
  }
}


// mostrar modal para crear lista
const showModalList = ref(false)


// validar si al grupo seleccionado ya se le añadió una descripción para mostrarla o pedirla si no
const showDescription = ref(false)
const pedirDescription = ref(false)

function showModalAddDescription() {
  if (descriptionSeleccionado.value === null || descriptionSeleccionado.value == '') {
    pedirDescription.value = true
  } else {
    showDescription.value = true
  }
}

function handleDescripcionCreada(nuevaDescripcion) {
  descriptionSeleccionado.value = nuevaDescripcion
}


// mostrar modal para eliminar grupo
const showModalDeleteGrupo = ref(false)

</script>


<template>
  <div class="home-container">
    <ModalCrearGrupo v-model="showModal" @grupoCreado="actualizarGrupos" />
    <div class="grupos">
      <div class="contenido-grupo">
        <div class="txtGrupoYCantidad">
          <h2>GRUPOS -</h2>
          <h2 class="h2ConEspacio">{{ cantidadDeGrupos }}</h2>
        </div>
        <hr />
        <ButtonComponent @click="showModal = true" txt="Añadir Grupo" />
        <div v-if="listaDeGrupos.length > 0">
          <TxtGrupoList v-for="g in listaDeGrupos" :key="g.id" :name="g.name" :value="g.id" @click="verGrupo(g)" class="listGrups" />
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
        <h2 v-if="seHaSeleccionado && listaDeGrupos.length > 0" class="h2ConEspacio">DE {{ nameEnMayusculas }}</h2>
      </div>
      <hr />
      <p v-if="listaDeGrupos.length === 0" class="no-listas">
        Aún no tienes ningun grupo, crea uno para empezar a crear listas y tareas
      </p>
      <p v-if="listaDeGrupos.length > 0 && !seHaSeleccionado" class="no-listas">
        Elije un grupo para ver sus listas y tareas
      </p>

      <div class="containerListasYButton" v-if="listaDeGrupos.length > 0 && seHaSeleccionado">
        <ListaComponent class="componenteLista" v-for="l in listaDeListas" :key="l.id" :name="l.name" :value="l.id" :description="l.description" :idDescription="idLista" />
        <ButtonComponent @click="showModalList = true" txt="Añadir lista" class="btnAddLista" />
      </div>

      <ModalCrearLista v-model="showModalList" :dato="idGrupo" />
      
      <div class="grupoDescription" v-if="seHaSeleccionado">
        <hr>
        <div class="txtDescript">
          <p class="accionGrupo" @click="showModalAddDescription">Descripción del grupo</p>
          <p class="separarAccionesGrupo"> - </p>
          <p class="accionGrupo" @click="showModalDeleteGrupo = true">Eliminar Grupo</p>
        </div>
        <ModalCrearDescripcionGrupo v-model="pedirDescription" :dato="idGrupo" @descripcionCreada="handleDescripcionCreada" />
        <VerDescription v-model="showDescription" h1="DESCRIPCIÓN DE ESTE GRUPO" :description="descriptionSeleccionado" />
        <ModalBorrarGrupo :dato="idGrupo" v-model="showModalDeleteGrupo" @grupoBorrado="actualizarGrupos" />
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
  display: flex;
  flex-direction: column;
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

.containerListasYButton {
  display: flex;
  gap: 20px;
}

.grupoDescription {
  margin-top: auto;
}

.txtDescript {
  display: flex;
  justify-content: center;
  font-weight: bold;
  font-size: 18px;
}

.txtDescript .accionGrupo:hover {
  color: rgb(206, 166, 166);
  cursor: pointer;
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

.componenteLista, .btnAddLista {
  width: 310px;
}

.separarAccionesGrupo {
  margin: 0px 15px;
}

</style>
