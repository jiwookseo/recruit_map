<template>
  <div class="outer">
    출발지를
    <strong>{{ getDepartureStationName }}역</strong>
    으로 변경했습니다!
  </div>
</template>

<script>
import { mapMutations, mapGetters } from 'vuex'
export default {
  name: 'StationAlert',
  computed: {
    ...mapGetters('localStorage', ['getDepartureStationName'])
  },
  created() {
    setTimeout(() => {
      this.closeAlert()
    }, 5000)
  },
  methods: {
    ...mapMutations('station', ['setShowStationAlert']),
    closeAlert() {
      this.setShowStationAlert(false)
    }
  }
}
</script>

<style lang="scss" scoped>
.outer {
  min-width: 100px;
  padding: 0 10px;
  height: 40px;
  line-height: 40px;
  border-radius: 2px;
  box-shadow: rgba(0, 0, 0, 0.3) 0px 1px 4px -1px;
  overflow: hidden;
  background: none rgb(255, 255, 255);
  margin: 10px;
  position: absolute;
  top: 0;
  right: 50px;
  cursor: pointer;
  user-select: none;
  font-size: 12px;
  text-align: center;
}
</style>
