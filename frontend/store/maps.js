export const state = () => ({
  // updated instantaneously realtime whenever map center is changed => @center_changed
  // used to update nearby company list shown in left sidebar
  centerLat: 37.5012,
  centerLng: 127.0396,

  // desired center of map
  // used to move map to specified region (e.g after user selects a particular company)
  detailLat: 0,
  detailLng: 0
})

export const getters = {
  getCenterLat: (state) => state.centerLat,
  getCenterLng: (state) => state.centerLng,
  getDetailLat: (state) => state.detailLat,
  getDetailLng: (state) => state.detailLng,
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
  },
  setDetailLat: (state, payload) => {
    state.detailLat = parseFloat(payload)
  },
  setDetailLng: (state, payload) => {
    state.detailLng = parseFloat(payload)
  }
}
export const actions = {}
