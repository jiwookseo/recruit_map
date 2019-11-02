export const state = () => ({
  searchShow: false
})

export const getters = {
  getSearchShow: (state) => state.searchShow
}

export const mutations = {
  setSearchShow: (state, payload) => {
    state.searchShow = payload
  }
}
export const actions = {}
