export const state = () => ({
  showSearchbar: false,
  showDefaultMenu: false
})

export const getters = {
  getShowSearchbar: (state) => state.showSearchbar,
  getShowDefaultMenu: (state) => state.showDefaultMenu
}

export const mutations = {
  setShowSearchbar: (state, payload) => {
    state.showSearchbar = payload
  },
  setShowDefaultMenu: (state, payload) => {
    state.showDefaultMenu = payload
  }
}
