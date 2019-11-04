<template>
  <GmapMarker
    :position="{ lat: marker.lat, lng: marker.lng }"
    :icon="markerOptions"
    :label="marker.name | truncateLabel"
    @mouseover="enableInfoWindow(marker)"
    @mouseout="disableInfoWindow"
    @click="infoDetail(marker)"
  />
</template>

<script>
import { mapMutations } from 'vuex'
export default {
  name: 'MapMarker',
  filters: {
    truncateLabel(label) {
      label = label.replace('(주)', '')
      if (label.length > 5) {
        label = label.substring(0, 4) + '...'
      }
      return label
    }
  },
  props: {
    marker: { type: Object, default: () => {} }
  },
  computed: {
    // Control marker shape (according to marker values)
    iconURL() {
      let url = 'default.png'
      if (!this.marker.jobs_count) {
        // If no current job openings
        url = 'disabled.png'
      } else if (this.marker.transitTime <= 30) {
        if (this.marker.avg_salary >= 5000) {
          url = 'closest_c2.png'
        } else if (this.marker.avg_salary >= 4000) {
          url = 'closest_c1.png'
        } else {
          url = 'closest.png'
        }
      } else if (this.marker.transitTime <= 45) {
        if (this.marker.avg_salary >= 5000) {
          url = 'closer_c2.png'
        } else if (this.marker.avg_salary >= 4000) {
          url = 'closer_c1.png'
        } else {
          url = 'closer.png'
        }
      } else if (this.marker.transitTime <= 60) {
        if (this.marker.avg_salary >= 5000) {
          url = 'close_c2.png'
        } else if (this.marker.avg_salary >= 4000) {
          url = 'close_c1.png'
        } else {
          url = 'close.png'
        }
      } else if (this.marker.avg_salary >= 5000) {
        url = 'default_c2.png'
      } else if (this.marker.avg_salary >= 4000) {
        url = 'default_c1.png'
      } else {
        url = 'default.png'
      }

      return url
    },
    markerOptions() {
      return {
        url: require(`~/static/${this.iconURL}`),
        size: { width: 68, height: 43, f: 'px', b: 'px' },
        scaledSize: { width: 68, height: 43, f: 'px', b: 'px' },
        labelOrigin: { x: 26, y: 27 }
      }
    }
  },
  methods: {
    ...mapMutations('infoWindow', [
      'setInfoWindowPosition',
      'setInfoWindowOptionsContent',
      'setShowInfoWindow'
    ]),
    ...mapMutations('company', ['setHoveredCompany', 'setCompanyDetail']),
    enableInfoWindow(marker) {
      this.setInfoWindowPosition({ lat: marker.lat, lng: marker.lng })
      this.setInfoWindowOptionsContent({
        name: marker.name,
        time: marker.transitTime,
        salary: marker.avg_salary,
        jobs: marker.jobs_count
      })
      this.setShowInfoWindow(true)
    },
    disableInfoWindow() {
      setTimeout(() => {
        this.setShowInfoWindow(false)
      }, 4000)
    },
    infoDetail(marker) {
      this.setCompanyDetail(marker)
      this.$router.push(`/company/${marker.id}/`)
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
