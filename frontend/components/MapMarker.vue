<template>
  <GmapMarker 
    :position="{ lat: marker.lat, lng: marker.lng }"
  />
</template>

<script>
export default {
  name: 'MapMarker',
  props: {
    marker: { type: Object }
  }
}
</script>

<style lang="scss" scoped></style>
