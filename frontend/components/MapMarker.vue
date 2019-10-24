<template>
  <GmapMarker
    :position="{ lat: marker.lat, lng: marker.lng }"
    :icon="markerOptions"
    :label="marker.name | truncateLabel"
    @mouseover="enableInfoWindow(marker)"
    @mouseout="disableInfoWindow"
  ></GmapMarker>
</template>

<script>
import { mapMutations } from 'vuex'
export default {
  name: 'MapMarker',
  props: {
    marker: { type: Object }
  },
  computed: {
    // Control marker shape (according to marker values)
    iconURL() {
      let url =
        'marker-gray.svg'
      if (this.marker.avg_salary > 5000) {
        url =
          'marker-star.svg'
      }
      else if (this.marker.avg_salary > 3500) {
        url =
          'marker-blue.svg'
      }
      return url
    },
    markerOptions() {
      return {
        url: require(`../static/${this.iconURL}`),
        size: { width: 80, height: 80, f: 'px', b: 'px' },
        scaledSize: { width: 80, height: 80, f: 'px', b: 'px' },
        // labelOrigin: {x: -2, y: 0}
      }
    }
  },
  methods: {
    ...mapMutations('infoWindow', [
      'setPosition',
      'setOptionsContent',
      'setOpen'
    ]),
    enableInfoWindow(marker) {
      this.setPosition({lat: marker.lat, lng: marker.lng})
      this.setOptionsContent({name: marker.name, time: marker.avg_salary})
      this.setOpen(true)
    },
    disableInfoWindow() {
      setTimeout(() => {
        this.setOpen(false)
      }, 200)
    }
  },
  filters: {
    truncateLabel(label) {
      label = label.replace("(주)", "")
      if (label.length > 5) {
        label = label.substring(0, 4) + '...'
      }
      return label
    }
  }
}
</script>

<style lang="scss">
// Marker Label Styling
#Default > div.vue-map-container > div.vue-map > div > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div > div > div > div {
  color: white !important;
  font-size: 0.9em !important;
  font-weight: bold;
}

</style>
