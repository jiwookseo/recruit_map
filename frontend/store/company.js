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
  setAsyncAllCompanies({ commit }, payload) {
    const res = api.getCompaniesData()
    res.then((v) => {
      commit('setAllCompanies', v.data)
    })
  }
}
