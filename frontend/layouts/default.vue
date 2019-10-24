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
      <MapMarker v-for="m in companyData" :key="m.id" :marker="m" />
      <MapInfoWindow />
    </GmapMap>
    <LeftSideBar />
    <nuxt />
  </div>
</template>

<script>
import MapMarker from '~/components/MapMarker.vue'
import MapInfoWindow from '~/components/MapInfoWindow.vue'
import companyData from '~/assets/company_data.js'
import LeftSideBar from '~/components/LeftSideBar'
export default {
  components: {
    MapMarker,
    MapInfoWindow,
    LeftSideBar
  },
  data() {
    return {
      companyData
    }
  }
}
</script>

<style lang="scss" scoped>
#Default {
  width: 100%;
  height: 100vh;
}
</style>
