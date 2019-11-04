import api from '../api/company'

export const state = () => ({
  hoveredCompany: {},
  selectedCompany: {},
  allCompanies: [],
  companyDetail: {}
})

export const getters = {
  getHoveredCompany: (state) => state.hoveredCompany,
  getSelectedCompany: (state) => state.selectedCompany,
  getAllCompanies: (state) => state.allCompanies,
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
  setCompanyDetail: (state, payload) => {
    state.companyDetail = payload
  }
}
export const actions = {
  async setAsyncAllCompanies({ commit, state, rootState }, payload) {
    const res = await api.getCompaniesData()
    const routes = rootState.station.routesFromStation
    res.data.forEach((c) => {
      const route = routes.find((r) => r.company === c.url)
      if (route) {
        c.transitTime = route.time
      }
    })
    commit('setAllCompanies', res.data)
  },
  async setAsyncCompanyDetail({ commit, dispatch }, payload) {
    const res = await api.getCompanyData(payload)
    commit('setCompanyDetail', res.data)
    dispatch('jobs/setAsyncJobData', res.data.jobs, { root: true })
    commit('maps/setTargetCenterLat', res.data.lat, { root: true })
    commit('maps/setTargetCenterLng', res.data.lng, { root: true })
  }
}
