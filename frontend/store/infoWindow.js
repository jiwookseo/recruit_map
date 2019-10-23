export const state = () => ({
  open: true,
  position: {
    lat: 37,
    lng: 127
  },
  // Info Window Content => Store each part into separate variables
  optionsContent: {
    t1: 'Initial t1',
    t2: 'Initial t2'
  }
})

export const getters = {
  open: (state) => state.open,
  position: (state) => state.position,
  optionsContent: (state) => state.optionsContent
}

export const mutations = {
  setOpen: (state, payload) => {
    state.Open = payload
  },
  setPosition: (state, payload) => {
    state.Position = payload
  },
  setOptionsContent: (state, payload) => {
    state.OptionsContent = payload
  }
}

export const actions = {
  setOpen({ commit }, payload) {
    // payload: Boolean value that controls whether or not info window is opened
    commit('setOpen', payload)
  },
  setPosition({ commit }, payload) {
    // payload: Object with lat and lng values
    commit('setPosition', payload)
  },
  setOptionsContent({ commit }, payload) {
    // payload: Object with t1 and t2 values
    commit('setOptionsContent', payload)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
