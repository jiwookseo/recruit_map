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
        lat: parseFloat(state.centerLat - 0.005).toFixed(7),
        lng: parseFloat(state.centerLng - 0.01).toFixed(7)
      },
      {
        lat: parseFloat(state.centerLat + 0.005).toFixed(7),
        lng: parseFloat(state.centerLng + 0.01).toFixed(7)
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
// 0.0043713
// 0.005
// 0.0095588
// 0.01
