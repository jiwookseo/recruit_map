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
      <MapMarker v-for="m in markers" :key="m.id" :marker="m" />
      <MapInfoWindow />
    </GmapMap>
  </div>
</template>

<script>
import MapMarker from '~/components/MapMarker.vue'
import MapInfoWindow from '~/components/MapInfoWindow.vue'

export default {
  components: {
    MapMarker,
    MapInfoWindow
  },
  data: () => ({
    markers: [
      {
        id: 1,
        lat: 37.5012,
        lng: 127.0396,
        name: 'marker1',
        label: 0
      },
      {
        id: 2,
        lat: 37.5012,
        lng: 127.042,
        name: 'marker2',
        label: 1
      },
      {
        id: 3,
        lat: 37.5012,
        lng: 127.044,
        name: 'marker3',
        label: 0
      }
    ],
    sampleText: 'Sample?',
    infoWinOpen: true,
    infoWindowPos: {
      lat: 37.5012,
      lng: 127.0396
    }
  }),
  computed: {
    infoOptions() {
      return {
        content: `<div class="infContainer"><div class="infWindow1">INFO WINDOW</div><div class="infWindow2">${this.sampleText}</div></div>`,
        pixelOffset: {
          width: 0,
          height: -35
        }
      }
    }
  }
}
</script>
