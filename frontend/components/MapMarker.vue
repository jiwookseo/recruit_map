<template>
  <GmapMarker
    :position="{ lat: marker.lat, lng: marker.lng }"
    :icon="markerOptions"
    :label="marker.name | truncateLabel"
    @mouseover="enableInfoWindow(marker)"
    @mouseout="disableInfoWindow"
  />
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
      let url = 'default.png'
      if (!this.marker.jobs_count) {
        // If no current job openings
        url = 'disabled.png'
      } 
      else if (this.marker.transitTime <= 30) {
        if (this.marker.avg_salary >= 5000) {
          url = 'closest_coin.png'
        }
        else {
          url = 'closest.png'
        }
      }
      else if (this.marker.transitTime <= 60) {
        if (this.marker.avg_salary >= 5000) {
          url = 'closer_coin.png'
        }
        else {
          url = 'closer.png'
        }
      }
      else {
        if (this.marker.avg_salary >= 5000) {
          url = 'default_coin.png'
        }
      }

      return url
    },
    markerOptions() {
      return {
        url: require(`../static/${this.iconURL}`),
        size: { width: 58, height: 42, f: 'px', b: 'px' },
        scaledSize: { width: 58, height: 42, f: 'px', b: 'px' },
        labelOrigin: {x: 26, y: 27}
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
      this.setPosition({ lat: marker.lat, lng: marker.lng })
      this.setOptionsContent({ 
        name: marker.name, 
        time: marker.transitTime,
        salary: marker.avg_salary,
        jobs: marker.jobs_count
      })
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
      label = label.replace('(주)', '')
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
#Default
  > div.vue-map-container
  > div.vue-map
  > div
  > div
  > div:nth-child(1)
  > div:nth-child(1)
  > div:nth-child(4)
  > div
  > div
  > div
  > div {
  color: white !important;
  font-size: 0.9em !important;
  font-weight: bold;
}
</style>
