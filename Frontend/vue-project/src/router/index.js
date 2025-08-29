import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import Home from '@/views/Home.vue'
import RecuperarPassword from '@/views/RecuperarPassword.vue'
import MsgActivarCuenta from '@/components/MsgActivarCuenta.vue'
import MsgRecuperarPdw from '@/components/MsgRecuperarPdw.vue'
import AddNewPwd from '@/views/AddNewPwd.vue'
import MsgPwdCambiada from '@/components/MsgPwdCambiada.vue'
import MsgSinAcceso from '@/components/MsgSinAcceso.vue'
import ModalCrearAlgo from '@/components/ModalCrearAlgo.vue'

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
      path: '/recuperarpassword',
      name: 'recuperarpassword',
      component: RecuperarPassword,
    },

    {
      path: '/msgactivarcuenta',
      name: 'msgactivarcuenta',
      component: MsgActivarCuenta,
    },

    {
      path: '/msgrecuperarpdw',
      name: 'msgrecuperarpdw',
      component: MsgRecuperarPdw,
    },

    {
      path: '/addnewpwd',
      name: 'addnewpwd',
      component: AddNewPwd,
    },

    {
      path: '/msgpwdcambiada',
      name: 'msgpwdcambiada',
      component: MsgPwdCambiada,
    },

    {
      path: '/msgsinacceso',
      name: 'msgsinacceso',
      component: MsgSinAcceso,
    },

    {
      path: '/modalcrearalgo',
      name: 'modalcrearalgo',
      component: ModalCrearAlgo,
      props: true
    },
  ],
})

export default router
