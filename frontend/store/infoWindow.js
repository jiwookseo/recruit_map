export const state = () => ({
  open: false,
  position: {
    lat: 37.5012,
    lng: 127.0396
  },
  // Info Window Content => Store each part into separate variables
  optionsContent: {
    name: 'Company Name',
    time: 'Transit Time'
  }
})

export const getters = {
  open: (state) => state.open,
  position: (state) => state.position,
  optionsContent: (state) => state.optionsContent
}

export const mutations = {
  setOpen: (state, payload) => {
    state.open = payload
  },
  setPosition: (state, payload) => {
    state.position = payload
  },
  setOptionsContent: (state, payload) => {
    state.optionsContent = payload
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
    // payload: Object with name and time values
    commit('setOptionsContent', payload)
  }
}
