<script setup>

</script>

<template>
  <div class="msg-container">
    <div class="email-box">
      <h1>REVISA TU CORREO ELECTRÓNICO</h1>
        <p id="text">Te hemos enviado un email al correo que ingresaste, ahora debes dar click en el enlace del email y así podrás recuperar tu contraseña.</p>
      <p><router-link to="/recuperarpassword">Volver</router-link></p>
    </div>
  </div>
</template>

<style scoped>
.msg-container {
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
