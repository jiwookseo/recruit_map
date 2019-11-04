export const state = () => ({
  showAboutUs: false
})

export const getters = {
  getShowAboutUs: (state) => state.showAboutUs
}

export const mutations = {
  setShowAboutUs: (state, payload) => {
    state.showAboutUs = payload
  }
}
