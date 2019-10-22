<template>
  <div>
    <LeftSideBar />
    <GmapMap
      :center="{ lat: 10, lng: 10 }"
      :zoom="7"
      map-type-id="terrain"
      style="width: 100vw; height: 100vh"
    ></GmapMap>
  </div>
</template>

<script>
import LeftSideBar from '../components/LeftSiderBar'
export default {
  components: {
    LeftSideBar
  }
}
</script>
