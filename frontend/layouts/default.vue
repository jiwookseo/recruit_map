<template>
  <div id="Default">
    <GmapMap
      ref="map"
      :center="{
        lat: getDetailLat || getLsMapCenterLat,
        lng: getDetailLng || getLsMapCenterLng
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
      <MapMarker v-for="m in this.getAllCompanies" :key="m.id" :marker="m" />
      <MapInfoWindow />
    </GmapMap>
    <LeftSidebar />
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
import { mapMutations, mapGetters, mapActions } from 'vuex'
import MapMarker from '~/components/MapMarker.vue'
import MapInfoWindow from '~/components/MapInfoWindow.vue'
import LeftSidebar from '~/components/LeftSidebar'
import StationButton from '~/components/StationButton.vue'
import StationMenu from '~/components/StationMenu.vue'
import StationAlert from '~/components/StationAlert.vue'
export default {
  components: {
    MapMarker,
    MapInfoWindow,
    LeftSidebar,
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
    ...mapGetters('localStorage', [
      'getDepartureStationID',
      'getLsMapCenterLat',
      'getLsMapCenterLng',
      'getLsMapZoom',
      'getFilteredCompanies'
    ]),
    ...mapGetters('station', [
      'getRoutesFromStation',
      'getAllStations',
      'getShowStationAlert',
      'getShowStationMenu'
    ]),
    ...mapGetters('maps', [
      'getCenterLat',
      'getCenterLng',
      'getDetailLat',
      'getDetailLng'
    ]),
    currentZoom() {
      return this.getLsMapZoom || 17
    },
    markerCompaniesData() {
      const data = this.getFilteredCompanies || this.getAllCompanies
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
    this.setCenterLat(this.getLsMapCenterLat)
    this.setCenterLng(this.getLsMapCenterLng)
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
      'setLsMapCenterLat',
      'setLsMapCenterLng',
      'setLsMapZoom'
    ]),
    ...mapMutations('station', [
      'setRoutesFromStation',
      'setAllStations',
      'setShowStationMenu'
    ]),
    ...mapMutations('maps', ['setCenterLat', 'setCenterLng']),
    center_changed() {
      const gMap = this.$refs.map
      this.setCenterLat(gMap.$mapObject.center.lat())
      this.setCenterLng(gMap.$mapObject.center.lng())
    },
    zoom_changed() {
      const gMap = this.$refs.map
      this.setLsMapZoom(gMap.$mapObject.zoom)
    },
    dragend() {
      const gMap = this.$refs.map
      this.setLsMapCenterLat(gMap.$mapObject.center.lat())
      this.setLsMapCenterLng(gMap.$mapObject.center.lng())
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
