import { ref } from "vue"
import api from "./axios"

// listar grupos
const grupo = ref([])

export const listarGrupos = async () => {
    try {
      let token = localStorage.getItem('access')
      const response = await api.get('/tareas/listar_grupos/',
        {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
  
      grupo.value = response.data
      
      if (grupo.value.length === 0) {
        console.log("No hay registros de grupos")
      } else {
        console.log("Sí hay registros de grupos")
      }
  
      console.log(grupo.value)
      return grupo.value
    } catch (error) {
      console.error(error)
    }
}

// listar cantidad de grupos
const cantGrups = ref(0)
export const listarCantidadGrupos = async () => {
  try {
    const grupos = await listarGrupos()

    cantGrups.value = grupos.length
    return cantGrups.value
  } catch (error) {
    console.error(error)
  }
}