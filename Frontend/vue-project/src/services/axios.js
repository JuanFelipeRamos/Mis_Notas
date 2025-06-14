import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
})

// Interceptor para añadir el token en las solicitudes
api.interceptors.request.use(config => {
  const token = localStorage.getItem('access')

  if (
    token &&
    !config.url.includes('/registro/') &&
    !config.url.includes('/token/')
  ) {
    config.headers.Authorization = `Bearer ${token}`
  }

  return config
})

// Interceptor para manejar errores y renovar el token si expiró
api.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config

    // Si recibimos 401 y no hemos intentado renovar el token todavía
    if (error.response && error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      try {
        const refresh = localStorage.getItem('refresh')

        // Llama al endpoint para renovar el token
        const res = await axios.post('http://localhost:8000/api/token/refresh/', {
          refresh: refresh
        })

        const newAccessToken = res.data.access
        localStorage.setItem('access', newAccessToken)

        // Actualiza el token y vuelve a intentar la solicitud original
        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`
        return api(originalRequest)
      } catch (refreshError) {
        console.error('Error al refrescar el token:', refreshError)

        // Borra los tokens si falló la renovación y redirige a login
        localStorage.removeItem('access')
        localStorage.removeItem('refresh')
        localStorage.removeItem('user')
        window.location.href = '/'
      }
    }

    return Promise.reject(error)
  }
)

export default api
