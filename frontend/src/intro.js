import Vue from 'vue'
import 'bootstrap/dist/css/bootstrap.css'

import introPage from './IntroPage.vue'

Vue.config.productionTip = false

new Vue({
    render: h => h(introPage),
}).$mount('#introPage')