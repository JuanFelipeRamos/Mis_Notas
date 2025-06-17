import { ref } from 'vue'

export function usePasswordToggle() {
  const mostrarPassword = ref(false)

  const togglePassword = () => {
    mostrarPassword.value = !mostrarPassword.value
  }

  return {
    mostrarPassword,
    togglePassword,
  }
}