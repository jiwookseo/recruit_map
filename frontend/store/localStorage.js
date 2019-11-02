export const state = () => ({
  departureStationID: 961,
  departureStationName: '역삼',
  
  // center & zoom level of last viewed map region
  // updated on map drag-end
  // stored in local storage to remember last map position upon page reload
  lsMapCenterLat: 37.5012,
  lsMapCenterLng: 127.0396,
  lsMapZoom: 0
})


export const getters = {
  getDepartureStationID: (state) => state.departureStationID,
  getDepartureStationName: (state) => state.departureStationName,
  getLsMapCenterLat: (state) => state.lsMapCenterLat,
  getLsMapCenterLng: (state) => state.lsMapCenterLng,
  getLsMapZoom: (state) => state.lsMapZoom,
}

export const mutations = {
  setDepartureStationID: (state, payload) => {
    state.departureStationID = payload
  },
  setDepartureStationName: (state, payload) => {
    state.departureStationName = payload
  },
  setLsMapCenterLat: (state, payload) => {
    state.lsMapCenterLat = payload
  },
  setLsMapCenterLng: (state, payload) => {
    state.lsMapCenterLng = payload
  },
  setLsMapZoom: (state, payload) => {
    state.lsMapZoom = payload
  },
}
