<template>
  <div id="Default">
    <GmapMap
      ref="map"
      :center="{ lat: 37.5012, lng: 127.0396 }"
      :zoom="17"
      map-type-id="roadmap"
      style="width: 100%; height: 100vh;"
      :options="{
        streetViewControl: false,
        fullscreenControl: false
      }"
    >
      <MapMarker v-for="m in getAllCompanies" :key="m.id" :marker="m" />
      <MapInfoWindow />
    </GmapMap>
    <LeftSideBar />
    <StationButton />
    <transition name="stationMenu">
      <StationMenu v-if="getShowStationMenu" />
    </transition>
    <nuxt />
  </div>
</template>

<script>
import axios from 'axios'
import { mapMutations, mapGetters } from 'vuex'
import MapMarker from '~/components/MapMarker.vue'
import MapInfoWindow from '~/components/MapInfoWindow.vue'
import LeftSideBar from '~/components/LeftSideBar'
import StationButton from '~/components/StationButton.vue'
import StationMenu from '~/components/StationMenu.vue'
export default {
  components: {
    MapMarker,
    MapInfoWindow,
    LeftSideBar,
    StationButton,
    StationMenu
  },
  data() {
    return {
      showStationMenu: false
    }
  },
  computed: {
    ...mapGetters('company', [
      'getAllCompanies',
    ]),
    ...mapGetters('station', [
      'getDepartureStationID',
      'getRoutesFromStation',
      'getAllStations',
      'getShowStationMenu'
    ]),
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
          let companies = res.data // Array of companies, WITHOUT transit time
          const routes = this.getRoutesFromStation // Routes with transit time info
          companies.forEach((c) => {
            // c.id = company id
            const route = routes.find(function(r) {
              return r.company === c.id
            })
            if (route) {
              c.transitTime = route.time;
            }
          })
          this.setAllCompanies(companies)
        })
      });
    
    // Get all station info
    axios.get(`${APIBase}stations/?all`)
      .then((res) => {
        this.setAllStations(res.data);
      });
  },
  methods: {
    ...mapMutations('company', [
      'setAllCompanies',
    ]),
    ...mapMutations('station', [
      'setDepartureStationID',
      'setRoutesFromStation',
      'setAllStations',
      'setShowStationMenu'
    ]),
    // center_changed() {
    //   console.log("CenterChanged")
    //   let a = this.$refs.map
    //   console.log(a.$mapObject)
    // },
    // bounds_changed() {
    //   console.log("BoundsChanged")
    // },
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
.stationMenu-enter-active {
  transition: all 0.6s ease;
}
.stationMenu-leave-active {
  transition: all 0.6s cubic-bezier(1, 0.5, 0.8, 1);
}
.stationMenu-enter,
.stationMenu-leave-to {
  transform: translateX(40px);
  opacity: 0;
}
</style>
