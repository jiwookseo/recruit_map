import api from '../api/station'

export const state = () => ({
  departureStationID: 961, // starting point
  departureStationName: '역삼',
  routesFromStation: [], // transit time info from specified station
  allStations: [],
  showStationMenu: false,
  showStationAlert: false
})

export const getters = {
  getDepartureStationID: (state) => state.departureStationID,
  getDepartureStationName: (state) => state.departureStationName,
  getRoutesFromStation: (state) => state.routesFromStation,
  getAllStations: (state) => state.allStations,
  getShowStationMenu: (state) => state.showStationMenu,
  getShowStationAlert: (state) => state.showStationAlert
}

export const mutations = {
  setDepartureStationID: (state, payload) => {
    state.departureStationID = payload
  },
  setDepartureStationName: (state, payload) => {
    state.departureStationName = payload
  },
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
  setAsyncDepartureStationID({ commit }, payload) {
    commit('setDepartureStationID', payload)
  },
  setAsyncDepartureStationName({ commit }, payload) {
    commit('setDepartureStationName', payload)
  },
  async setAsyncRoutesFromStation({ commit, state }, payload) {
    const res = await api.getStationRoutes(payload.v)
    commit('setRoutesFromStation', res.data.results)
    payload.cb()
  },
  async setAsyncAllStations({ commit }, payload) {
    const res = await api.getAllStation()
    commit('setAllStations', res.data)
  },
  setShowStationMenu({ commit }, payload) {
    commit('setShowStationMenu', payload)
  }
}
