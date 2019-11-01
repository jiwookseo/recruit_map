import axios from 'axios'

export default {
  getJobData: (url) => {
    return axios.get(url)
  }
}
