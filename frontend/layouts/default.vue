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
      @center_changed="center_changed"
    >
      <!-- @bounds_changed="bounds_changed" -->
      <MapMarker v-for="m in getAllCompanies" :key="m.id" :marker="m" />
      <MapInfoWindow />
    </GmapMap>
    <LeftSideBar />
    <StationButton />
    <transition name="stationMenu">
      <StationMenu v-if="getShowStationMenu" />
    </transition>
    <transition name="stationMenu">
      <StationAlert v-if="getShowStationAlert" />
    </transition>
    <nuxt />
  </div>
</template>

<script>
import axios from 'axios'
import { mapMutations, mapGetters, mapActions } from 'vuex'
import MapMarker from '~/components/MapMarker.vue'
import MapInfoWindow from '~/components/MapInfoWindow.vue'
import LeftSideBar from '~/components/LeftSideBar'
import StationButton from '~/components/StationButton.vue'
import StationMenu from '~/components/StationMenu.vue'
import StationAlert from '~/components/StationAlert.vue'
export default {
  components: {
    MapMarker,
    MapInfoWindow,
    LeftSideBar,
    StationButton,
    StationMenu,
    StationAlert
  },
  data() {
    return {
      showStationMenu: false
    }
  },
  computed: {
    ...mapGetters('company', ['getAllCompanies']),
    ...mapGetters('station', [
      'getDepartureStationID',
      'getRoutesFromStation',
      'getAllStations',
      'getShowStationAlert',
      'getShowStationMenu'
    ])
  },
  methods: {
    ...mapActions('station', [
      'setAsyncRoutesFromStation',
      'setAsyncAllStations'
    ]),
    ...mapActions('company', ['setAsyncAllCompanies']),
    ...mapMutations('company', ['setAllCompanies']),
    ...mapMutations('station', [
      'setDepartureStationID',
      'setRoutesFromStation',
      'setAllStations',
      'setShowStationMenu'
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
  },
  created() {
    // TODO: Check local storage to see if departure station has been previously set
    const stationID = this.getDepartureStationID || 961
    this.setAsyncAllStations()
    this.setAsyncRoutesFromStation(stationID)
    this.setAsyncAllCompanies()
  }
}

// Get all station info
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
