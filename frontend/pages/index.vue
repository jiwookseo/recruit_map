<template>
  <div>
    <LeftSideBar />
    <GmapMap
      :center="{ lat: 37.5012, lng: 127.0396 }"
      :zoom="17"
      map-type-id="roadmap"
      style="width: 100%; height: 100vh;"
    >
      <!-- <GmapMarker :position="position" />
      <GmapMarker
        v-for="m in markers"
        :key="m.id"
        :position="{ lat: m.lat, lng: m.lng }"
      />-->
      <MapMarker v-for="m in markers" :key="m.id" :marker="m" />
      <!-- <GmapInfoWindow
        :options="infoOptions"
        :position="infoWindowPos"
        :opened="infoWinOpen"
      >
      </GmapInfoWindow>-->
      <MapInfoWindow />
    </GmapMap>
  </div>
</template>

<script>
import LeftSideBar from '../components/LeftSiderBar'
import MapMarker from '~/components/MapMarker.vue'
import MapInfoWindow from '~/components/MapInfoWindow.vue'

export default {
  components: {
    MapMarker,
    MapInfoWindow,
    LeftSideBar
  },
  data: () => ({
    // position: { lat: 37.501, lng: 127.0396 },
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

<style lang="scss">
.infContainer {
  // position: absolute;
  width: 100px;
  height: 100px;
  // top: 50%; left: 50%;
  // transform: translate(-50%, -50%);
  background: white;
}
.infWindow1 {
  color: red;
}
.infWindow2 {
  color: blue;
}
.gm-style .gm-style-iw-c {
  width: 100px !important;
  height: 100px !important;
  background: white;
  padding: 0 !important;
  border-radius: 3px !important;
  button {
    display: none !important;
  }
}
</style>
