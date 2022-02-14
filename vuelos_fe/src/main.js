import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
//import { BFormSelect } from 'bootstrap-vue'
//Vue.component('b-form-select', BFormSelect)

createApp(App).use(router).mount('#app')
