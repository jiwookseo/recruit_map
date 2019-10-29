<template>
  <div id="Default">
    <GmapMap
      ref="map"
      :center="{ lat: 37.5012, lng: 127.0396 }"
      :zoom="17"
      map-type-id="roadmap"
      style="width: 100%; height: 100vh;"
      :options="{
        streetViewControl: false
      }"
      @center_changed="center_changed"
    >
      <!-- @bounds_changed="bounds_changed" -->
      <MapMarker v-for="m in getAllCompanies" :key="m.id" :marker="m" />
      <MapInfoWindow />
    </GmapMap>
    <LeftSideBar />
    <nuxt />
  </div>
</template>

<script>
import axios from 'axios'
import { mapMutations, mapGetters } from 'vuex'
import MapMarker from '~/components/MapMarker.vue'
import MapInfoWindow from '~/components/MapInfoWindow.vue'
import LeftSideBar from '~/components/LeftSideBar'
export default {
  components: {
    MapMarker,
    MapInfoWindow,
    LeftSideBar
  },
  data() {
    return {}
  },
  computed: {
    ...mapGetters('company', [
      'getAllCompanies',
      'getDepartureStationID',
      'getRoutesFromStation'
    ])
  },
  created() {
    // API Base URL
    const APIBase = 'http://52.78.29.170:8000/api/'

    // TODO: Check local storage to see if departure station has been previously set
    // const localStorageStationID = window.localStorage.getItem("gmapDepartureStation")

    // Set departure station => 역삼(961) as default
    // let stationID = localStorageStationID ? localStorageStationID : 600
    const stationID = this.getDepartureStationID

    // Retrieve routes from above station and store in Vuex
    axios
      .get(`${APIBase}stations/${stationID}/routes`)
      .then((res) => {
        this.setRoutesFromStation(res.data)
      })
      .then(() => {
        // Retrieve all company data from DB (including transit time) and store in Vuex
        axios.get(`${APIBase}companies/?all`).then((res) => {
          const companies = res.data // Array of companies, WITHOUT transit time
          const routes = this.getRoutesFromStation // Routes with transit time info
          companies.forEach((c) => {
            // c.id = company id
            const route = routes.find(function(r) {
              return r.company === c.id
            })
            c.transitTime = route.time
          })
          this.setAllCompanies(companies)
        })
      })
  },
  methods: {
    ...mapMutations('company', [
      'setAllCompanies',
      'setDepartureStationID',
      'setRoutesFromStation'
    ]),
    ...mapMutations('maps', ['setCenterLat', 'setCenterLng']),
    center_changed() {
      let gMap = this.$refs.map
      this.setCenterLat(gMap.$mapObject.center.lat())
      this.setCenterLng(gMap.$mapObject.center.lng())
    }
    // bounds_changed() {
    //   console.log('BoundsChanged')
    // }
    // geolocate() {  // finds actual location of user
    //   navigator.geolocation.getCurrentPosition(pos => {
    //     console.log("lat: ", pos.coords.latitude);
    //     console.log("lng: ", pos.coords.longitude);
    //   })
    // }
  }
}
</script>

<style lang="scss" scoped>
#Default {
  width: 100%;
  height: 100vh;
}
</style>
