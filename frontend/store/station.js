export const state = () => ({
  routesFromStation: [], // transit time info from specified station
  departureStationID: 961 // starting point
})

export const getters = {
  getDepartureStationID: (state) => state.departureStationID,
  getRoutesFromStation: (state) => state.routesFromStation,
}

export const mutations = {
  setDepartureStationID: (state, payload) => {
    state.departureStationID = payload
  },
  setRoutesFromStation: (state, payload) => {
    state.routesFromStation = payload
  },
}
export const actions = {
  setDepartureStationID({
    commit
  }, payload) {
    commit('setDepartureStationID', payload)
  },
  setRoutesFromStation({
    commit
  }, payload) {
    commit('setRoutesFromStation', payload)
  },
}
