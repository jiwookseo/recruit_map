export const state = () => ({
  hoveredCompany: {},
  selectedCompany: {},
  allCompanies: [],
  routesFromStation: [], // transit time info from specified station
  companyDetail: {},
  departureStationID: 961 // starting point
})

export const getters = {
  getHoveredCompany: (state) => state.hoveredCompany,
  getSelectedCompany: (state) => state.selectedCompany,
  getAllCompanies: (state) => state.allCompanies,
  getDepartureStationID: (state) => state.departureStationID,
  getRoutesFromStation: (state) => state.routesFromStation,
  getCompanyDetail: (state) => state.companyDetail
}

export const mutations = {
  setHoveredCompany: (state, payload) => {
    state.hoveredCompany = payload
  },
  setSelectedCompany: (state, payload) => {
    state.selectedCompany = payload
  },
  setAllCompanies: (state, payload) => {
    state.allCompanies = payload
  },
  setDepartureStationID: (state, payload) => {
    state.departureStationID = payload
  },
  setRoutesFromStation: (state, payload) => {
    state.routesFromStation = payload
  },
  setCompanyDetail: (state, payload) => {
    state.companyDetail = payload
  }
}
export const actions = {
  setAllCompanies({
    commit
  }, payload) {
    commit('setAllCompanies', payload)
  },
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
  setCompanyDetail({
    commit
  }, payload) {
    commit('setCompanyDetail', payload)
  }
}
