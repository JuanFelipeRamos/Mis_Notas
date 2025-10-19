<script setup>
import ButtonComponent from './ButtonComponent.vue';

</script>


<template>
    <div class="container">
        <div class="containerNameLista">
            <p class="nameLista">Análisis</p>
        </div>
        <div class="containerTareas">
            <ol>
                <li>Levantar requerimientos</li>
                <li>Diagramar requerimientos</li>
            </ol>
            <div class="btnTareas">
                <button>Añadir tarea</button>
            </div>
        </div>
        <ButtonComponent txt="Eliminar lista" />
    </div>
</template>


<style scoped>
.container {
    display: flex;
    flex-direction: column;
}

.containerNameLista {
    background-color: #b67e3d;
    color: black;
    padding: 12px;
    width: 100%;
    font-weight: bold;
    border-radius: 8px;
    text-align: center;
}

.containerTareas {
    display: flex;
    flex-direction: column;
    background-color: #b67e3d;
    margin: 7px 0px;
    border-radius: 8px;
    height: 230px;
    justify-content: space-between;
}

ol {
    list-style-position: inside;
    margin: 0;
    padding: 0;
}

li {
    color: black;
    font-weight: bold;
    font-size: 15px;
    margin-top: 7px;
    margin-left: 15px;
}

.btnTareas {
    display: flex;
    justify-content: center;
}

button {
    background-color: #c79f6e;
    color: black;
    padding: 8px;
    margin: 16px 0px;
    width: 70%;
    font-weight: bold;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #bb925f;
}

</style>