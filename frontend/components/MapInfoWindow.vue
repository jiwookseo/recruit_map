<template>
  <GmapInfoWindow 
    :options="options" 
    :position="position" 
    :opened="open"
    @mouseover="enableInfoWindow"
    @mouseout="disableInfoWindow"
    @click="test"
  ></GmapInfoWindow>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'

export default {
  name: 'MapInfoWindow',
  computed: {
    ...mapGetters({
      open: 'infoWindow/getOpen',
      position: 'infoWindow/getPosition',
      optionsContent: 'infoWindow/getOptionsContent'
    }),
    options() {
      return {
        content: `<div class="infWinContainer"><div class="r1">${this.optionsContent.name}</div><div class="r2">${this.optionsContent.time}분</div></div>`,
        pixelOffset: {
          width: 0,
          height: -60
        }
      }
    }
  },
  methods: {
    ...mapMutations('infoWindow', ['setOpen']),
    enableInfoWindow() {
      console.log("hover infowindow")
      this.setOpen(true);
    },
    disableInfoWindow() {
      setTimeout(() => {
        this.setOpen(false)
      }, 200)
    },
    test() {
      console.log("CLICK TEST")
    }
  }
}
</script>

<style lang="scss">
//// Global CSS Styling /////

// 1) Override default info window styles
.gm-style .gm-style-iw-c {
  min-width: 160px !important;
  height: auto !important;
  background: white;
  padding: 0 !important;
  border-radius: 3px !important;
  button {
    display: none !important;
  }
  & > .gm-style-iw-d,
  & > .gm-style-iw-d > div {
    min-width: 160px !important;
    height: auto !important;
    overflow-x: hidden !important;
  }
}

// 2) Control internal content styles, i.e options.content
.infWinContainer {
  width: 100%;
  height: auto;
  background: white;
  padding: 10px;
  & > .r1 {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
    white-space: nowrap;
  }
  & > .r2 {
  }
}
</style>
