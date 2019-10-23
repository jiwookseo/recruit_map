<template>
  <div class="left--side-bar">
    <InputDiv />
    <CompanyInfoDiv />
    <Recruit />
  </div>
</template>

<script>
import InputDiv from './InputDiv'
import CompanyInfoDiv from './CompanyInfoDiv'
import Recruit from './Recruit'
export default {
  name: 'LeftSideBar',
  components: {
    InputDiv,
    CompanyInfoDiv,
    Recruit
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
  z-index: 999999;
  border-radius: 4px;
}
</style>
