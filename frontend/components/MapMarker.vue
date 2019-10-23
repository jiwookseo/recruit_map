<template>
  <GmapMarker
    :position="{ lat: marker.lat, lng: marker.lng }"
    :title="marker.name"
    :icon="markerOptions"
  >
  </GmapMarker>
</template>

<script>
export default {
  name: 'MapMarker',
  props: {
    marker: { type: Object }
  },
  data: () => ({}),
  computed: {
    // Control marker shape (according to marker values)
    iconURL() {
      let url = 'https://maps.google.com/mapfiles/kml/shapes/library_maps.png'
      if (this.marker.label) {
        url = 'https://maps.google.com/mapfiles/kml/shapes/parking_lot_maps.png'
      }
      return url
    },
    markerOptions() {
      return {
        url: this.iconURL,
        size: { width: 30, height: 30, f: 'px', b: 'px' },
        scaledSize: { width: 30, height: 30, f: 'px', b: 'px' }
      }
    }
  }
}
</script>

<style lang="scss">
.infWindowBox {
  width: 100px;
  height: 100px;
  position: absolute;
  bottom: 100%;
  background: white;
}
</style>
