<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../services/axios'
import { usePasswordToggle } from '@/services/verPassword'

const route = useRoute()
const router = useRouter()

const uidb64 = route.query.uidb64
const token = route.query.token

console.log("uidb64:", uidb64)
console.log("token:", token)

const usuario = ref({
  password: '',
  passwordConfirmada: ''
})

const recuperarPassword = async () => {
  if (usuario.value.password !== usuario.value.passwordConfirmada){
    console.log("error, las contraseñas no coinciden")
    alert("Error, las contraseñas ongresadas no coinciden entre ellas, deben ser iguales")
    return
  }

  try {
    const response = await api.post(`/usuarios/recuperar_pwd/${uidb64}/${token}/`, {
      password: usuario.value.password
    })
    
    console.log(response.data)

    usuario.value = {
      password: ''
    }

    router.push('/msgpwdcambiada')
  } catch (error) {
    console.error("Error al recuperar contraseña:", error)
    alert("Hubo un problema al cambiar tu contraseña.")
  }
}

// Para mostrar o no el texto que se escribe en el input de contraseña
const { mostrarPassword, togglePassword } = usePasswordToggle()

</script>

<template>
  <div class="pwd-container">
    <div class="pwd-box">
      <h1>RECUPERA TU CONTRASEÑA</h1>
      <form @submit.prevent="recuperarPassword">
        <p>Aquí puedes ingresar una nueva contraseña para asignarla a tu cuenta, recomendado que la contraseña sea fácil de recordar (anotala en un lugar seguro).</p>
        <div class="input-password-container">
          <input
            v-model="usuario.password"
            :type="mostrarPassword ? 'text' : 'password'"
            placeholder="NUEVA CONTRASEÑA"
          />
          <span class="material-symbols-outlined icono-ojo" @click="togglePassword">
            {{ mostrarPassword ? 'visibility' : 'visibility_off' }}
          </span>

          <input
            v-model="usuario.passwordConfirmada"
            :type="mostrarPassword ? 'text' : 'password'"
            placeholder="CONFIRMAR NUEVA CONTRASEÑA"
          />
          <span class="material-symbols-outlined icono-ojo" @click="togglePassword">
            {{ mostrarPassword ? 'visibility' : 'visibility_off' }}
          </span>
        </div>
        
        <button>CONTINUAR</button>
      </form>
      <p><router-link to="/">Volver</router-link></p>
    </div>
  </div>
</template>

<style scoped>
.pwd-container {
  height: 100vh;
  background-color: #2b0000;
  display: flex;
  justify-content: center;
  align-items: center;
}

.pwd-box {
  background-color: #c3863f;
  padding: 45px 40px;
  text-align: center;
  border-radius: 12px;
  width: 400px;
}

.pwd-box h1 {
  font-size: 24px;
  margin-bottom: 30px;
  font-weight: bold;
  color: #000;
}

.pwd-box input {
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

.pwd-box button {
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

.pwd-box p {
  margin-top: 25px;
  font-size: 16px;
  color: #000;
}

.pwd-box a {
  text-decoration: none;
  color: inherit;
}

.pwd-box a:hover,
.link:hover {
  color: white;
}
</style>
