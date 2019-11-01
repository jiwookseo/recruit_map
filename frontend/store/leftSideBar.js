export const state = () => ({
  defaultMenu: true,
  searchShow: false
})

export const getters = {
  getDefaultMenu: (state) => state.defaultMenu,
  getSearchShow: (state) => state.searchShow
}

export const mutations = {
  setDefaultMenu: (state, payload) => {
    state.defaultMenu = payload
  },
  setSearchShow: (state, payload) => {
    state.searchShow = payload
  }
}
export const actions = {}
