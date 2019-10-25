export const state = () => ({
  hoveredCompany: {},
  selectedCompany: {},
  allCompanies: [],
  routesFromStation: [] // transit time info from specified station
})

export const getters = {
  getHoveredCompany: (state) => state.hoveredCompany,
  getSelectedCompany: (state) => state.selectedCompany,
  getAllCompanies: (state) => state.allCompanies,
  getRoutesFromStation: (state) => state.routesFromStation,
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
  setRoutesFromStation: (state, payload) => {
    state.routesFromStation = payload
  }
}
export const actions = {
  setAllCompanies({
    commit
  }, payload) {
    commit('setAllCompanies', payload)
  },
  setRoutesFromStation({
    commit
  }, payload) {
    commit('setRoutesFromStation', payload)
  },
}
