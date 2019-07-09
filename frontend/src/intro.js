import Vue from 'vue'

import introPage from './introPage.vue'

Vue.config.productionTip = false

new Vue({
    render: h => h(introPage),
}).$mount('#introPage')