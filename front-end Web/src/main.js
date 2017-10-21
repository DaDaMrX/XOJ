import Vue from 'vue'
import app from './app.vue'

import axios from 'axios'
Vue.prototype.$ajax = axios

new Vue({
  el: '#app',
  render: h => h(app)
})