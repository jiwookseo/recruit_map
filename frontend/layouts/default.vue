<template>
  <div id="Default">
    <client-only>
      <GmapMap
        ref="map"
        :center="{
          lat: getTargetCenterLat || getLastCenterLat,
          lng: getTargetCenterLng || getLastCenterLng
        }"
        :zoom="currentZoom"
        map-type-id="roadmap"
        style="width: 100%; height: 100vh;"
        :options="{
          streetViewControl: false,
          fullscreenControl: false
        }"
        @center_changed="center_changed"
        @zoom_changed="zoom_changed"
        @dragend="dragend"
      >
        <!-- @bounds_changed="bounds_changed" -->

        <MapMarker v-for="m in markerCompaniesData" :key="m.id" :marker="m" />
        <MapInfoWindow />
      </GmapMap>
    </client-only>
    <LeftSidebar />
    <StationButton />
    <transition name="stationMenu">
      <StationMenu v-if="getShowStationMenu" />
    </transition>
    <transition name="stationMenu">
      <StationAlert v-if="getShowStationAlert" />
    </transition>
    <AboutUs v-if="getShowAboutUs" />
    <nuxt />
  </div>
</template>

<script>
import { mapMutations, mapGetters, mapActions } from 'vuex'
import MapMarker from '~/components/Map/MapMarker.vue'
import MapInfoWindow from '~/components/Map/MapInfoWindow.vue'
import LeftSidebar from '~/components/LeftSidebar'
import StationButton from '~/components/Station/StationButton.vue'
import StationMenu from '~/components/Station/StationMenu.vue'
import StationAlert from '~/components/Station/StationAlert.vue'
import AboutUs from '~/components/AboutUs'
export default {
  components: {
    MapMarker,
    MapInfoWindow,
    LeftSidebar,
    StationButton,
    StationMenu,
    StationAlert,
    AboutUs
  },
  data() {
    return {
      showStationMenu: false
    }
  },
  computed: {
    ...mapGetters('company', ['getAllCompanies']),
    ...mapGetters('localStorage', [
      'getDepartureStationID',
      'getLastCenterLat',
      'getLastCenterLng',
      'getLastZoom',
      'getFilteredCompanies'
    ]),
    ...mapGetters('station', [
      'getRoutesFromStation',
      'getAllStations',
      'getShowStationAlert',
      'getShowStationMenu'
    ]),
    ...mapGetters('maps', [
      'getRealtimeCenterLat',
      'getRealtimeCenterLng',
      'getTargetCenterLat',
      'getTargetCenterLng'
    ]),
    ...mapGetters('about', [
      'getShowAboutUs',
    ]),
    currentZoom() {
      return this.getLastZoom || 17
    },
    markerCompaniesData() {
      const data =
        this.getFilteredCompanies.length >= 1
          ? this.getFilteredCompanies
          : this.getAllCompanies
      return data
    }
  },
  created() {
    const stationID = this.getDepartureStationID
    this.setAsyncAllStations()
    this.setAsyncRoutesFromStation({
      v: stationID,
      cb: this.setAsyncAllCompanies
    })
    this.setRealtimeCenterLat(this.getLastCenterLat)
    this.setRealtimeCenterLng(this.getLastCenterLng)
  },
  methods: {
    ...mapActions('station', [
      'setAsyncRoutesFromStation',
      'setAsyncAllStations'
    ]),
    ...mapActions('company', ['setAsyncAllCompanies']),
    ...mapMutations('company', ['setAllCompanies']),
    ...mapMutations('localStorage', [
      'setDepartureStationID',
      'setLastCenterLat',
      'setLastCenterLng',
      'setLastZoom'
    ]),
    ...mapMutations('station', [
      'setRoutesFromStation',
      'setAllStations',
      'setShowStationMenu'
    ]),
    ...mapMutations('maps', ['setRealtimeCenterLat', 'setRealtimeCenterLng']),
    center_changed() {
      const gMap = this.$refs.map
      this.setRealtimeCenterLat(gMap.$mapObject.center.lat())
      this.setRealtimeCenterLng(gMap.$mapObject.center.lng())
    },
    zoom_changed() {
      const gMap = this.$refs.map
      this.setLastZoom(gMap.$mapObject.zoom)
    },
    dragend() {
      const gMap = this.$refs.map
      this.setLastCenterLat(gMap.$mapObject.center.lat())
      this.setLastCenterLng(gMap.$mapObject.center.lng())
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
  overflow: hidden;
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
