export const state = () => ({
  departureStationID: 961, // starting point
  departureStationName: '역삼',
  routesFromStation: [], // transit time info from specified station
  allStations: [],
  showStationMenu: false,
  showStationAlert: false,
})

export const getters = {
  getDepartureStationID: (state) => state.departureStationID,
  getDepartureStationName: (state) => state.departureStationName,
  getRoutesFromStation: (state) => state.routesFromStation,
  getAllStations: (state) => state.allStations,
  getShowStationMenu: (state) => state.showStationMenu,
  getShowStationAlert: (state) => state.showStationAlert,
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
  },
}
// export const actions = {
//   setDepartureStationID({
//     commit
//   }, payload) {
//     commit('setDepartureStationID', payload)
//   },
//   setDepartureStationName({
//     commit
//   }, payload) {
//     commit('setDepartureStationName', payload)
//   },
//   setRoutesFromStation({
//     commit
//   }, payload) {
//     commit('setRoutesFromStation', payload)
//   },
//   setAllStations({
//     commit
//   }, payload) {
//     commit('setAllStations', payload)
//   },
//   setShowStationMenu({
//     commit
//   }, payload) {
//     commit('setShowStationMenu', payload)
//   },
//   setShowStationAlert({
//     commit
//   }, payload) {
//     commit('setShowStationAlert', payload)
//   },
// }
