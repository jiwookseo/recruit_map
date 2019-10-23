<template>
  <div>
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
  </div>
</template>

<script>
import MapMarker from '~/components/MapMarker.vue'
import MapInfoWindow from '~/components/MapInfoWindow.vue'
import companyData from '~/assets/company_data.js'

export default {
  components: {
    MapMarker,
    MapInfoWindow
  },
  data() {
    return {
      companyData
    }
  }
}
</script>
