<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/axios';

const router = useRouter()
const usuario = ref({
  email: ''
})

const recuperarPassword = async (e) => {
  e.preventDefault()

  try {
    // Para enviar correo de activación de cuenta
    const response = await api.post('/usuarios/msg_recuperar_pwd/', {
      email: usuario.value.email
    })

    usuario.value.email = ''

    router.push('/msgrecuperarpdw')
  } catch (error) {
    alert('Ocurrió un error al solicitar la recuperación de contraseña.')
    console.error('Error:', error)
    if (error.response && error.response.data) {
      console.log("Detalles del backend:", error.response.data.detalle);
    }
  }
}

</script>

<template>
  <div class="password-container">
    <div class="email-box">
      <h1>RECUPERA TU CONTRASEÑA</h1>
      <form @submit.prevent="recuperarPassword">
        <p id="text">Ingresa tu correo electrónico para que te enviemos un enlace donde podrás recuperar tu contraseña.</p>
        <input v-model="usuario.email" type="email" placeholder ="CORREO ELECTRÓNICO" required />

        <button>CONTINUAR</button>
      </form>
      <p><router-link to="/">Volver</router-link></p>
    </div>
  </div>
</template>

<style scoped>
.password-container {
  height: 100vh;
  background-color: #2b0000;
  display: flex;
  justify-content: center;
  align-items: center;
}

.email-box {
  background-color: #c3863f;
  padding: 45px 40px;
  text-align: center;
  border-radius: 12px;
  width: 400px;
}

.email-box h1 {
  font-size: 24px;
  margin-bottom: 30px;
  font-weight: bold;
  color: #000;
}

.email-box input {
  display: block;
  width: 100%;
  padding: 12px;
  margin: 10px 0;
  border-radius: 8px;
  border: none;
  font-size: 14px;
}

.email-box button {
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

.email-box p {
  margin-top: 25px;
  font-size: 16px;
  color: #000;
}

#text {
  margin-bottom: 15px;
}

.email-box a {
  text-decoration: none;
  color: inherit;
}

.email-box a:hover {
  color: white;
}

</style>
