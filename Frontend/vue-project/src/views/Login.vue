<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/axios'

const router = useRouter()
const usuario = ref({
  username: '',
  password: ''
})

const login = async () => {
  try {
    const response = await api.post('/token/', {
      username: usuario.value.username,
      password: usuario.value.password,
    })

    // Guardar tokens en localStorage
    localStorage.setItem('access', response.data.access)
    localStorage.setItem('refresh', response.data.refresh)

    console.log('Inicio de sesión exitoso')
    router.push('/home') // Redirige a la página de inicio

  } catch (error) {
    alert('Error al iniciar sesión')
    console.error(error)
  }
}

</script>

<template>
  <div class="login-container">
    <div class="login-box">
      <h1>INICIA SESIÓN</h1>
      <form @submit.prevent="login">
        <input v-model="usuario.username" type="text" placeholder="NOMBRE DE USUARIO" />
        <input v-model="usuario.password" type="password" placeholder="CONTRASEÑA" />
        <button>CONTINUAR</button>
      </form>
      <p>O crea una cuenta <router-link to="/register">aquí</router-link></p>
    </div>
  </div>
</template>

<style scoped>
.login-container {
  height: 100vh;
  background-color: #2b0000;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-box {
  background-color: #c3863f;
  padding: 45px 40px;
  text-align: center;
  border-radius: 12px;
  width: 400px;
}

.login-box h1 {
  font-size: 24px;
  margin-bottom: 30px;
  font-weight: bold;
  color: #000;
}

.login-box input {
  display: block;
  width: 100%;
  padding: 12px;
  margin: 10px 0;
  border-radius: 8px;
  border: none;
  font-size: 14px;
}

.login-box button {
  background-color: #5d0000;
  color: white;
  border: none;
  padding: 12px;
  width: 100%;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  margin-top: 20px;
}

.login-box p {
  margin-top: 25px;
  font-size: 16px;
  color: #000;
}

.login-box p a {
  text-decoration: none;
  color: inherit;
}

.login-box p a:hover {
  color: white;
}

</style>
