<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const isLoggedIn = ref(true)

const router = useRouter()

function logout() {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
  isLoggedIn.value = false
  router.push('/')
  console.log('Sesión cerrada con éxito')
}
</script>


<template>
  <div class="home-container">
    <div class="grupos">
      <div class="contenido-grupo">
        <h2>GRUPOS</h2>
        <hr />
        <button class="btn-grupo">Añadir grupo</button>
      </div>

      <div class="cerrar-sesion">
        <hr />
        <a href="#" @click.prevent="logout">Cerrar sesión</a>
      </div>
    </div>

    <div class="listas">
      <h2>TUS LISTAS</h2>
      <hr />
      <p class="no-listas">Aún no tienes ninguna lista</p>
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
