import axios from 'axios'
const BASE_URL = 'http://52.78.29.170:8000/api/'

export default {
  getStationRoutes(id) {
    console.log('STATION ROUTE API CALL WITH AXIOS')
    const data = axios.get(`${BASE_URL}stations/${id}/routes/`)
    return data
  },
  getAllStation() {
    console.log('ALL STATION API CALL WITH AXIOS')
    const data = axios.get(`${BASE_URL}stations/?all`)
    return data
  }
}
