<template>
  <div class="left--side-bar">
    <InputDiv />
    <CompanyInfoDiv v-if="getDefaultMenu" />
    <Recruit v-if="getDefaultMenu" />
  </div>
</template>

<script>
import InputDiv from './InputDiv'
import CompanyInfoDiv from './CompanyInfoDiv'
import Recruit from './Recruit'
import { mapGetters } from 'vuex'
export default {
  name: 'LeftSideBar',
  components: {
    InputDiv,
    CompanyInfoDiv,
    Recruit
  },
  computed: {
    ...mapGetters('leftSideBar', ['getDefaultMenu'])
  }
}
</script>

<style lang="scss" >
.left--side-bar {
  display: flex;
  flex-direction: column;
  width: 380px;
  height: 300px;
  position: absolute;
  top: 10px;
  left: 10px;
  z-index: 999999;
  border-radius: 4px;
}
</style>
