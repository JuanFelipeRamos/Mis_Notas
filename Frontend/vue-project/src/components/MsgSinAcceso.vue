<script setup>

</script>

<template>
  <div class="msg-container">
    <div class="sinAccess-box">
      <h1>SIN ACCESO</h1>
        <p id="text">No has iniciado sesión, debes hacerlo para poder ingresar a la aplicación.</p>

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

.sinAccess-box {
  background-color: #c3863f;
  padding: 45px 40px;
  text-align: center;
  border-radius: 12px;
  width: 400px;
}

.sinAccess-box h1 {
  font-size: 24px;
  margin-bottom: 30px;
  font-weight: bold;
  color: #000;
}

.sinAccess-box p {
  margin-top: 25px;
  font-size: 16px;
  color: #000;
}

#text {
  margin-bottom: 15px;
}

.sinAccess-box a {
  text-decoration: none;
  color: inherit;
}

.sinAccess-box a:hover {
  color: white;
}

</style>
