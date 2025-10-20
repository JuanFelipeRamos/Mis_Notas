import { ref } from "vue";
import api from "./axios";

export const listarListasDeUnGrupo = async (id) => {
    const listas = ref([])
    try {
        const response = await api.get(`/tareas/listas_de_grupo/?id_grupo=${id}`)
        listas.value = response.data
        return listas.value
    } catch (error) {
        console.log("Error al listar las listas de este grupo", error)
    }
}
