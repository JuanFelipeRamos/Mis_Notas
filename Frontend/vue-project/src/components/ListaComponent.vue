<script setup>
import { ref } from 'vue';
import ButtonComponent from './ButtonComponent.vue';
import VerDescription from './VerDescription.vue';
import ModalCrearDescriptionLista from './ModalCrearDescriptionLista.vue';

const showDescription = ref(false)
const showModalCrearDescription = ref(false)
const hayTareas = ref(false)
const props = defineProps({
    name: String,
    listaDeTareas: Array,
    description: String,
    idLista: Number
})

if (!props.listaDeTareas || props.listaDeTareas.length === 0) {
    hayTareas.value = false
} else {
    hayTareas.value = true
}

function verModalDescription() {
    if (props.description != '') {
        showDescription.value = true
    }

    if (!props.description || props.description.trim() === '') {
        showModalCrearDescription.value = true
    }
}

</script>


<template>
    <div class="container">
        <VerDescription v-model="showDescription" h1="DESCRIPCIÓN DE ESTA LISTA" :description="description" />
        <ModalCrearDescriptionLista v-model="showModalCrearDescription" :dato="props.idLista" />
        <div class="containerNameLista">
            <p class="nameLista" @click="verModalDescription">{{ name }}</p>
        </div>
        <div class="containerTareas">
            <ol v-if="hayTareas">
                <li>{{ listaDeTareas }}</li>
            </ol>
            <p v-if="hayTareas == false">Esta lista no tiene tareas</p>
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

.nameLista {
    cursor: pointer;
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

.containerTareas p {
    color: black;
    text-align: center;
    margin-top: 10px;
    font-size: 15px;
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