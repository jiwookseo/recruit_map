<template>
  <div class="left--side-bar" :style="{ zIndex: getShowSearchbar ? 11 : 7}">
    <InputDiv />
    <FilterList v-show="getShowDefaultMenu" />
    <CompanyInfo v-show="getShowDefaultMenu" />
    <Recruit v-show="getShowDefaultMenu" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import FilterList from './FilterList'
import InputDiv from './InputDiv'
import CompanyInfo from './CompanyInfo'
import Recruit from './Recruit'
export default {
  name: 'LeftSidebar',
  components: {
    FilterList,
    InputDiv,
    CompanyInfo,
    Recruit
  },
  computed: {
    ...mapGetters('leftSidebar', ['getShowDefaultMenu', 'getShowSearchbar'])
  },
}
</script>

<style lang="scss">
.left--side-bar {
  display: flex;
  flex-direction: column;
  width: 380px;
  height: 300px;
  position: absolute;
  top: 10px;
  left: 10px;
  z-index: 7;
  border-radius: 4px;
}
</style>
