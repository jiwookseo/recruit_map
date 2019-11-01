import api from '../api/job'

export const state = () => ({
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
