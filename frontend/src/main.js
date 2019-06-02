import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import axios from 'axios'
import VueAxios from 'vue-axios'

export const EventBus = new Vue()

Vue.use(VueAxios, axios);

import App from './App.vue'

Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
    render: h => h(App),
}).$mount('#app')