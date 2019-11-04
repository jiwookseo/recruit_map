import api from '../api/station'

export const state = () => ({
  // departure station related states are stored in localStorage.js
  routesFromStation: [], // transit time info from specified station
  allStations: [],
  showStationMenu: false,
  showStationAlert: false
})

export const getters = {
  getRoutesFromStation: (state) => state.routesFromStation,
  getAllStations: (state) => state.allStations,
  getShowStationMenu: (state) => state.showStationMenu,
  getShowStationAlert: (state) => state.showStationAlert
}

export const mutations = {
  setRoutesFromStation: (state, payload) => {
    state.routesFromStation = payload
  },
  setAllStations: (state, payload) => {
    state.allStations = payload
  },
  setShowStationMenu: (state, payload) => {
    state.showStationMenu = payload
  },
  setShowStationAlert: (state, payload) => {
    state.showStationAlert = payload
  }
}
export const actions = {
  async setAsyncRoutesFromStation({ commit, state }, payload) {
    const res = await api.getStationRoutes(payload.v)
    commit('setRoutesFromStation', res.data.results)
    payload.cb()
  },
  async setAsyncAllStations({ commit }, payload) {
    const res = await api.getAllStation()
    commit('setAllStations', res.data)
  }
}
