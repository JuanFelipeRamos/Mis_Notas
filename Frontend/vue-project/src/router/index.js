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
import ModalCrearGrupo from '@/components/ModalCrearGrupo.vue'
import TxtGrupoList from '@/components/TxtGrupoList.vue'
import ButtonComponent from '@/components/ButtonComponent.vue'
import ModalCrearLista from '@/components/ModalCrearLista.vue'
import ModalCrearDescripcionGrupo from '@/components/ModalCrearDescripcionGrupo.vue'
import VerDescription from '@/components/VerDescription.vue'
import ModalBorrarGrupo from '@/components/ModalBorrarGrupo.vue'
import ListaComponent from '@/components/ListaComponent.vue'

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
      path: '/modalcreargrupo',
      name: 'modalcreargrupo',
      component: ModalCrearGrupo,
    },

    {
      path: '/txtgrupolist',
      name: 'txtgrupolist',
      component: TxtGrupoList,
      props: true
    },

    {
      path: '/buttoncomponent',
      name: 'buttoncomponent',
      component: ButtonComponent,
      props: true
    },

    {
      path: '/modalcrearlista',
      name: 'modalcrearlista',
      component: ModalCrearLista,
    },

    {
      path: '/modalcreardescripciongrupo',
      name: 'modalcreardescripciongrupo',
      component: ModalCrearDescripcionGrupo,
      props: true
    },

    {
      path: '/verdescription',
      name: 'verdescription',
      component: VerDescription,
      props: true
    },

    {
      path: '/modalborrargrupo',
      name: 'modalborrargrupo',
      component: ModalBorrarGrupo,
      props: true
    },

    {
      path: '/listacomponent',
      name: 'listacomponent',
      component: ListaComponent
    },

  ],
})

export default router
