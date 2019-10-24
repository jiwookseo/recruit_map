<template>
  <GmapMarker
    :position="{ lat: marker.lat, lng: marker.lng }"
    :icon="markerOptions"
    :label="'can you see it'"
    @mouseover="enableInfoWindow(marker)"
    @mouseout="disableInfoWindow"
  ></GmapMarker>
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
      let url =
        'https://img.pngio.com/surrounding-environment-svg-png-icon-free-download-377100-png-icon-980_932.png'
      if (this.marker.avg_salary > 4000) {
        url =
          'https://img.pngio.com/an-crown-crown-glasses-icon-with-png-and-vector-format-for-free-crown-icon-png-512_365.png'
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
        time: marker.avg_salary
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
