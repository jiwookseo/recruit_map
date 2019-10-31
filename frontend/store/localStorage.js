export const state = () => ({
  departureStationID: 961,
  departureStationName: '역삼'
})


export const getters = {
  getDepartureStationID: (state) => state.departureStationID,
  getDepartureStationName: (state) => state.departureStationName,
}

export const mutations = {
  setDepartureStationID: (state, payload) => {
    state.departureStationID = payload
  },
  setDepartureStationName: (state, payload) => {
    state.departureStationName = payload
  },
}
