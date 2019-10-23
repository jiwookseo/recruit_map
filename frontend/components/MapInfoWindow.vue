<template>
  <GmapMarker
    :options="optionsContent"
    :position="position"
    :opened="open"
  ></GmapMarker>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'MapInfoWindow',
  props: {
    info: { type: Object }
  },
  computed: {
    ...mapGetters('infoWindow', ['open', 'position', 'optionsContent']),
    infWinOptions() {
      return {
        content: `<div class="infContainer"><div class="infWindow1">${this.infWinOptionsContent.t1}</div><div class="infWindow2">${this.infWinOptionsContent.t2}</div></div>`,
        pixelOffset: {
          width: 0,
          height: -35
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped></style>
