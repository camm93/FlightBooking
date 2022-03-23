import { createRouter, createWebHashHistory } from 'vue-router'

import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'
import Vuelos from './components/Vuelos.vue'
import Home from './components/Home.vue'
import Account from './components/Account.vue'
import Reservas from './components/Reservas.vue'

const routes = [
  {
    path: '/user/logIn',
    name: "logIn",
    component: LogIn
  },
  {
    path: '/user/signUp',
    name: "signUp",
    component: SignUp
  },
  {
    path: '/vuelos',
    name: "vuelos",
    component: Vuelos
  },
  {
    path: '/user/home',
    name: "home",
    component: Home
  },
  {
    path: '/user/account',
    name: "account",
    component: Account
  },
  {
    path: '/user/reservas',
    name: "reservas",
    component: Reservas
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
