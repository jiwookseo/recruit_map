import axios from 'axios'
const BASE_URL = 'http://52.78.29.170:8000/api/'

export default {
  getStationRoutes(id) {
    const data = axios.get(`${BASE_URL}stations/${id}/routes/`)
    return data
  },
  getAllStation() {
    const data = axios.get(`${BASE_URL}stations/?all`)
    return data
  }
}
