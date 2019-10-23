<template>
  <GmapMarker
    :position="{ lat: marker.lat, lng: marker.lng }"
    :title="marker.name"
    :icon="markerOptions"
    @mouseover="enableInfoWindow(marker)"
    @mouseout="disableInfoWindow"
  >
  </GmapMarker>
</template>

<script>
export default {
  name: 'MapMarker',
  props: {
    marker: { type: Object }
  },
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
  },
  methods: {
    enableInfoWindow(marker) {
      this.$store.dispatch('infoWindow/setPosition', {
        lat: marker.lat,
        lng: marker.lng
      })
      this.$store.dispatch('infoWindow/setOptionsContent', {
        name: marker.name,
        time: marker.label
      })
      this.$store.dispatch('infoWindow/setOpen', true)
    },
    disableInfoWindow() {
      setTimeout(() => {
        this.$store.dispatch('infoWindow/setOpen', false)
      }, 200)
    }
  }
}
</script>

<style lang="scss"></style>
