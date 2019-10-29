import axios from 'axios'
const BASE_URL = 'http://52.78.29.170:8000/api/'

export default {
  async getCompanyData(id) {
    const data = await axios.get(`${BASE_URL}companies/${id}`)
    return data
  },
  async getCompaniesData() {
    const data = await axios.get(`${BASE_URL}companies/?all`)
    return data
  }
}
