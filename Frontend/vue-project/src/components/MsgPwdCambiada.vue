<script setup>

</script>

<template>
  <div class="msg-container">
    <div class="msg-box">
      <h1>Tu contraseña se cambió exitosamente</h1>
        <p id="text">Ya puedes iniciar sesión con tu nueva contraseña.</p>
      <p><router-link to="/">Iniciar sesión</router-link></p>
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

.msg-box {
  background-color: #c3863f;
  padding: 45px 40px;
  text-align: center;
  border-radius: 12px;
  width: 400px;
}

.msg-box h1 {
  font-size: 24px;
  margin-bottom: 30px;
  font-weight: bold;
  color: #000;
}

.msg-box p {
  margin-top: 25px;
  font-size: 16px;
  color: #000;
}

#text {
  margin-bottom: 15px;
}

.msg-box a {
  text-decoration: none;
  color: inherit;
}

.msg-box a:hover {
  color: white;
}

</style>
