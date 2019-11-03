<template>
  <div
    class="outer"
    :class="{ on: getShowStationMenu }"
    @click.stop="showStationMenuToggle"
  >
    <i class="material-icons-round">directions_subway</i>
  </div>
</template>

<script>
import { mapMutations, mapGetters } from 'vuex'

export default {
  name: 'StationButton',
  props: {
    mode: { type: Boolean, default: false }
  },
  computed: {
    ...mapGetters('station', ['getShowStationMenu'])
  },
  methods: {
    ...mapMutations('station', ['setShowStationMenu']),
    showStationMenuToggle() {
      if (this.getShowStationMenu) {
        this.setShowStationMenu(false)
      } else {
        this.setShowStationMenu(true)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.outer {
  width: 40px;
  height: 40px;
  border-radius: 2px;
  box-shadow: rgba(0, 0, 0, 0.3) 0px 1px 4px -1px;
  overflow: hidden;
  background: none rgb(255, 255, 255);
  margin: 10px;
  position: absolute;
  top: 0;
  right: 0;
  cursor: pointer;
  user-select: none;
  & > i {
    color: #666666;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  &.on {
    background: #666666;
    & > i {
      color: white;
    }
  }
}
</style>
