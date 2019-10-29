import axios from 'axios'
const BASE_URL = 'http://52.78.29.170:8000/api/'

export default {
  async getStationRoutes(id) {
    const data = await axios.get(`${BASE_URL}stations/${id}/routes/`)
    return data
  },
  async getAllStation() {
    const data = axios.get(`${BASE_URL}stations/?all`)
    return data
  }
}
