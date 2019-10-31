<template>
  <div class="left--side-bar">
    <InputDiv />
    <CompanyInfo v-show="getDefaultMenu" />
    <Recruit v-show="getDefaultMenu" />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import InputDiv from './InputDiv'
import CompanyInfo from './CompanyInfo'
import Recruit from './Recruit'
export default {
  name: 'LeftSideBar',
  components: {
    InputDiv,
    CompanyInfo,
    Recruit
  },
  computed: {
    ...mapGetters('leftSideBar', ['getDefaultMenu'])
  }
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
