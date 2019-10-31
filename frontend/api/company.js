import axios from 'axios'
const BASE_URL = 'http://52.78.29.170:8000/api/companies'

export default {
  getCompanyDataByName(params) {
    console.log(name)
    return axios.get(`${BASE_URL}/`, {
      params: {
        name: params
      }
    })
  },
  getCompanyData(id) {
    return axios.get(`${BASE_URL}/${id}`)
  },
  getCompaniesData() {
    return axios.get(`${BASE_URL}/?all`)
  }
}
