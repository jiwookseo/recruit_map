import axios from 'axios'
const BASE_URL = 'http://recruitmap.ninja:8000/api/'

export default {
  getCompanyDataByName: (name) =>
    new Promise(async (resolve, reject) => {
      const res = await axios.get(BASE_URL)
      const API = res.data
      resolve(axios.get(API.companies, { params: { name } }))
    }),
  getCompanyData: (id) =>
    new Promise(async (resolve, reject) => {
      const res = await axios.get(BASE_URL)
      const API = res.data
      resolve(axios.get(`${API.companies}/${id}/`))
    }),
  getCompaniesData: () =>
    new Promise(async (resolve, reject) => {
      const res = await axios.get(BASE_URL)
      const API = res.data
      resolve(axios.get(`${API.companies}/?all`))
    })
}
