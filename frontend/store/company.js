export const state = () => ({
  hoveredCompany: {},
  selectedCompany: {}
})

export const getters = {
  getHoveredCompany: (state) => state.hoveredCompany,
  getSelectedCompany: (state) => state.selectedCompany
}

export const mutations = {
  setHoveredCompany: (state, payload) => {
    state.hoveredCompany = payload
  },
  setSelectedCompany: (state, payload) => {
    state.selectedCompany = payload
  }
}
export const actions = {}
