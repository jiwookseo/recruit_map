import Vue from 'vue'
import Vuex from 'vuex'
import infoWindow from './modules/infoWindow'
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    infoWindow
  }
})
