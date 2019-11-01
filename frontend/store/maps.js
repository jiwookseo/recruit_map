export const state = () => ({
  centerLat: 37.5012,
  centerLng: 127.0396
})

export const getters = {
  getCenterLat: (state) => state.centerLat,
  getCenterLng: (state) => state.centerLng,
  getLatLng: (state) => {
    return [
      {
        lat: parseFloat(parseFloat(state.centerLat - 0.005).toFixed(7)),
        lng: parseFloat(parseFloat(state.centerLng - 0.0035).toFixed(7))
      },
      {
        lat: parseFloat(parseFloat(state.centerLat + 0.005).toFixed(7)),
        lng: parseFloat(parseFloat(state.centerLng + 0.0035).toFixed(7))
      }
    ]
  }
}

export const mutations = {
  setCenterLat: (state, payload) => {
    state.centerLat = payload
  },
  setCenterLng: (state, payload) => {
    state.centerLng = payload
  }
}
export const actions = {}
