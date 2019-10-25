<template>
  <div id="Default">
    <GmapMap
      :center="{ lat: 37.5012, lng: 127.0396 }"
      :zoom="17"
      map-type-id="roadmap"
      style="width: 100%; height: 100vh;"
      :options="{
        streetViewControl: false
      }"
    >
      <MapMarker v-for="m in getAllCompanies" :key="m.id" :marker="m" />
      <MapInfoWindow />
    </GmapMap>
    <LeftSideBar />
    <nuxt />
  </div>
</template>

<script>
import MapMarker from '~/components/MapMarker.vue'
import MapInfoWindow from '~/components/MapInfoWindow.vue'
// import companyData from '~/assets/company_data.js'
import LeftSideBar from '~/components/LeftSideBar'
import axios from 'axios'
import { mapMutations, mapGetters } from 'vuex'
export default {
  components: {
    MapMarker,
    MapInfoWindow,
    LeftSideBar
  },
  data() {
    return {
      // companyData
    }
  },
  computed: {
    ...mapGetters('company', ['getAllCompanies', 'getRoutesFromStation'])
  },
  methods: {
    ...mapMutations('company', [
      'setAllCompanies',
      'setRoutesFromStation'
    ]),
  },
  created() {
    // API Base URL
    const APIBase = "http://52.78.29.170:8000/api/"

    // Check local storage to see if departure station has been previously set 
    const localStorageStationID = window.localStorage.getItem("gmapDepartureStation")

    // Set departure station. If null, set 역삼(961) as default station
    let stationID = localStorageStationID ? localStorageStationID : 600

    // Retrieve routes from above station and store in Vuex
    axios.get(`${APIBase}stations/${stationID}/routes`)
      .then((res) => {
        this.setRoutesFromStation(res.data);
      })

    // Retrieve all company data from DB (including transit time) and store in Vuex
    axios.get(`${APIBase}companies/?all`)
      .then((res) => {
        let companies = res.data;  // Array of companies, WITHOUT transit time
        const routes = this.getRoutesFromStation;  // Routes with transit time info
        companies.forEach((c) => {  // c.id = company id
          const route = routes.find(function(r) {
            return r.company === c.id
          });
          c.transitTime = route.time
        })
        this.setAllCompanies(companies);
        console.log("Vuex getAllCompanies", this.getAllCompanies)
      });
  }
}
</script>

<style lang="scss" scoped>
#Default {
  width: 100%;
  height: 100vh;
}
</style>
