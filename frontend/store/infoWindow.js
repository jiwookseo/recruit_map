export const state = () => ({
  showInfoWindow: false,
  infoWindowPosition: {
    lat: 37.5012,
    lng: 127.0396
  },
  infoWindowOptionsContent: {}
})

export const getters = {
  getShowInfoWindow: (state) => state.showInfoWindow,
  getInfoWindowPosition: (state) => state.infoWindowPosition,
  getInfoWindowOptionsContent: (state) => state.infoWindowOptionsContent
}

export const mutations = {
  setShowInfoWindow: (state, payload) => {
    state.showInfoWindow = payload
  },
  setInfoWindowPosition: (state, payload) => {
    state.infoWindowPosition = payload
  },
  setInfoWindowOptionsContent: (state, payload) => {
    state.infoWindowOptionsContent = payload
  }
}
