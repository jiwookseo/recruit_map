// gogo;
import axios from 'axios'
const BASE_URL = 'http://52.78.29.170:8000/api/'

export default {
  async getCompanyData(id) {
    return await axios.get(`${BASE_URL}companies/${id}`)
  }
}
