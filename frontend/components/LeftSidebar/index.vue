<template>
  <div class="left--side-bar" :style="{ zIndex: getShowSearchbar ? 11 : 7 }">
    <InputDiv />
    <CompanyInfo v-show="getShowDefaultMenu" />
    <FilterList v-show="getShowDefaultMenu" />
    <Recruit v-show="getShowDefaultMenu" />
    <transition name="fade">
      <NoData v-if="getNoDataAlert" />
    </transition>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import FilterList from './FilterList'
import InputDiv from './InputDiv'
import CompanyInfo from './CompanyInfo'
import Recruit from './Recruit'
import NoData from './NoData'
export default {
  name: 'LeftSidebar',
  components: {
    FilterList,
    InputDiv,
    CompanyInfo,
    Recruit,
    NoData
  },
  computed: {
    ...mapGetters('leftSidebar', [
      'getShowSearchbar',
      'getShowDefaultMenu',
      'getNoDataAlert'
    ])
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
  // overflow: hidden;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.7s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
