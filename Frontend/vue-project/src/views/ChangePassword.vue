<script setup>
import { ref } from 'vue'
import { usePasswordToggle } from '@/services/verPassword'

const usuario = ref({
  password_actual: '',
  password_nueva: '',
  password_confirmar: '',
})

// Para mostrar o no el texto que se escribe en el input de contraseña
const { mostrarPassword, togglePassword } = usePasswordToggle()

</script>

<template>
  <div class="login-container">
    <div class="email-box">
      <h1>CAMBIA TU CONTRASEÑA</h1>
      <form>
        <div class="input-password-container">
          <input
            v-model="usuario.password_actual"
            :type="mostrarPassword ? 'text' : 'password'"
            placeholder="CONTRASEÑA ACTUAL"
          />
          <span class="material-symbols-outlined icono-ojo" @click="togglePassword">
            {{ mostrarPassword ? 'visibility' : 'visibility_off' }}
          </span>
        </div>

        <div class="input-password-container">
          <input
            v-model="usuario.password_nueva"
            :type="mostrarPassword ? 'text' : 'password'"
            placeholder="NUEVA CONTRASEÑA"
          />
          <span class="material-symbols-outlined icono-ojo" @click="togglePassword">
            {{ mostrarPassword ? 'visibility' : 'visibility_off' }}
          </span>
        </div>

        <div class="input-password-container">
          <input
            v-model="usuario.password_confirmar"
            :type="mostrarPassword ? 'text' : 'password'"
            placeholder="CONFIRMAR CONTRASEÑA"
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
.login-container {
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

.input-password-container {
  position: relative;
}

.input-password-container input {
  padding-right: 40px; /* espacio para el ícono */
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

.email-box a {
  text-decoration: none;
  color: inherit;
}

.email-box a:hover {
  color: white;
}

</style>
