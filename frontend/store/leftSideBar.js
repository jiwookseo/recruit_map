export const state = () => ({
  defaultMenu: true
})

export const getters = {
  getDefaultMenu: (state) => state.defaultMenu
}

export const mutations = {
  setDefaultMenu: (state, payload) => {
    state.defaultMenu = payload
  }
}
export const actions = {}
