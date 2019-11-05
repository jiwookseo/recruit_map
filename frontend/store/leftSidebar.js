export const state = () => ({
  showSearchbar: false,
  showDefaultMenu: true,
  noDataAlert: false
})

export const getters = {
  getShowSearchbar: (state) => state.showSearchbar,
  getShowDefaultMenu: (state) => state.showDefaultMenu,
  getNoDataAlert: (state) => state.noDataAlert
}

export const mutations = {
  setShowSearchbar: (state, payload) => {
    state.showSearchbar = payload
  },
  setShowDefaultMenu: (state, payload) => {
    state.showDefaultMenu = payload
  },
  setNoDataAlert: (state, payload) => {
    state.noDataAlert = payload
  }
}
