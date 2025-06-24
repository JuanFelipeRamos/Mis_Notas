import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Home from '@/views/Home.vue'
import ChangePassword from '@/views/ChangePassword.vue'
import MsgActivarCuenta from '@/views/MsgActivarCuenta.vue'
import CuentaActivada from '@/views/CuentaActivada.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login,
    },

    {
      path: '/register',
      name: 'register',
      component: Register,
    },

    {
      path: '/home',
      name: 'home',
      component: Home,
    },

    {
      path: '/changepassword',
      name: 'changepassword',
      component: ChangePassword,
    },

    {
      path: '/msgactivarcuenta',
      name: 'msgactivarcuenta',
      component: MsgActivarCuenta,
    },
    
    {
      path: '/cuentaactivada/:uid/:token',
      name: 'cuentaactivada',
      component: CuentaActivada,
    },
  ],
})

export default router
