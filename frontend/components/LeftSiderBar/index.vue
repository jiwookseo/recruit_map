<template>
  <div class="left--side-bar">
    <h1>Hello World</h1>

    <InputDiv />
  </div>
</template>

<script>
import InputDiv from './InputDiv'
export default {
  name: 'LeftSideBar',
  components: {
    InputDiv
  }
}
</script>

<style lang="scss">
.left--side-bar {
  display: flex;
  flex-direction: column;
  width: 350px;
  height: 160px;
  position: absolute;
  top: 10px;
  left: 10px;
  background-color: #8774c1;
  z-index: 999999;
  border-radius: 4px;
}
</style>
