<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'
import api from '../services/axios';
import { usePasswordToggle } from '@/services/verPassword'

const router = useRouter()
const usuario = ref({
  username: "",
  first_name: "",
  last_name: "",
  email: "",
  password: ""
});

const registrarUsuario = async (e) => {
  e.preventDefault()

  try {
    const response = await api.post('/usuarios/registro/', usuario.value)
    const email = usuario.value.email
    //alert('Registro de usuario exitoso, ya puedes iniciar sesión.')

    // Para enviar correo de activación de cuenta
    await api.post('/usuarios/msg_validar_email/', {
      email: email
    })

    usuario.value = {
      username: '',
      first_name: '',
      last_name: '',
      email: '',
      password: ''
    }

    router.push('/msgactivarcuenta')
  } catch (error) {
    alert('Ocurrió un error al registrar el usuario.')
    console.error('Error al registrar:', error)
    if (error.response && error.response.data) {
      console.log("Detalles del backend:", error.response.data.detalle);
    }
  }
}

// Aquí función para consumir API de envío de correo para verificación y activación de cuenta ---------->

// Para mostrar o no el texto que se escribe en el input de contraseña
const { mostrarPassword, togglePassword } = usePasswordToggle()

</script>

<template>
  <div class="registro-container">
    <div class="formulario">
      <h1>REGÍSTRATE</h1>
      <form @submit.prevent="registrarUsuario">
        <input v-model="usuario.username" type="text" placeholder ="NOMBRE DE USUARIO" required />
        <input v-model="usuario.first_name" type="text" placeholder ="NOMBRES" required />
        <input v-model="usuario.last_name" type="text" placeholder="APELLIDOS" />
        <input v-model="usuario.email" type="email" placeholder ="CORREO ELECTRÓNICO" required />

        <div class="input-password-container">
          <input
            v-model="usuario.password"
            :type="mostrarPassword ? 'text' : 'password'"
            placeholder="CONTRASEÑA"
            required
          />
          <span class="material-symbols-outlined icono-ojo" @click="togglePassword">
            {{ mostrarPassword ? 'visibility' : 'visibility_off' }}
          </span>
        </div>

        <button>CONTINUAR</button>
      </form>
      <p>O inicia sesión <router-link to="/">aquí</router-link></p>
    </div>
  </div>
</template>

<style scoped>
.registro-container {
  height: 100vh;
  background-color: #2b0000;
  display: flex;
  justify-content: center;
  align-items: center;
}

.formulario {
  background-color: #c3863f;
  padding: 45px 40px;
  text-align: center;
  border-radius: 12px;
  width: 400px;
}

.formulario h1 {
  font-size: 24px;
  margin-bottom: 30px;
  font-weight: bold;
  color: #000;
}

.formulario input {
  display: block;
  width: 100%;
  padding: 12px;
  margin: 10px 0;
  border-radius: 8px;
  border: none;
  font-size: 14px;
}

.input-password-container {
  position: relative;
}

.input-password-container input {
  padding-right: 40px;
}

.icono-ojo {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  color: #555;
  font-size: 24px;
}

.formulario button {
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

.formulario p {
  margin-top: 25px;
  font-size: 16px;
  color: #000;
}

.formulario a {
  text-decoration: none;
  color: inherit;
}

.formulario a:hover,
.link:hover {
  color: white;
}

</style>
