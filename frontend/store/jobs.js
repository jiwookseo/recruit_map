import api from '../api/job'

export const state = () => ({
  // all open job positions of the selected company displayed in left sidebar
  jobData: []
})

export const getters = {
  getJobData: (state) => state.jobData
}

export const mutations = {
  setJobData: (state, payload) => {
    state.jobData = payload
  }
}
export const actions = {
  async setAsyncJobData({ commit }, payload) {
    const data = await api.getJobData(payload)
    commit('setJobData', data.data.results)
  }
}
