import axios from 'axios'
const BASE_URL = 'http://52.78.29.170:8000/api/'

export default {
  getCompanyData(id) {
    return axios.get(`${BASE_URL}companies/${id}`)
  },
  getCompaniesData() {
    return axios.get(`${BASE_URL}companies/?all`)
  }
}
