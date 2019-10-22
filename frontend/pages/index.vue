<template>
  <div>
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
      /> -->
      <MapMarker v-for="m in markers" :key="m.id" :marker="m" />
    </GmapMap>
  </div>
</template>

<script>
import MapMarker from '~/components/MapMarker.vue'

export default {
  components: {
    MapMarker
  },
  data: () => ({
    position: { lat: 37.501, lng: 127.0396 },
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
    ]
  })
}
</script>
