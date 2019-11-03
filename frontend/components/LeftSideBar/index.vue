<template>
  <div class="left--side-bar" :style="{ zIndex: getShowSearchbar ? 11 : 7}">
    <InputDiv />
    <CompanyInfo v-show="getShowDefaultMenu" />
    <Recruit v-show="getShowDefaultMenu" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import InputDiv from './InputDiv'
import CompanyInfo from './CompanyInfo'
import Recruit from './Recruit'
export default {
  name: 'LeftSidebar',
  components: {
    InputDiv,
    CompanyInfo,
    Recruit
  },
  computed: {
    ...mapGetters('leftSidebar', ['getShowDefaultMenu', 'getShowSearchbar'])
  }
}
</script>

<style lang="scss">
.left--side-bar {
  display: flex;
  flex-direction: column;
  width: 360px;
  height: calc(100vh - 20px);
  position: absolute;
  top: 10px;
  left: 10px;
  z-index: 7;
  overflow: hidden;
}
</style>
