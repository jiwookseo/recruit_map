<template>
  <div class="outer">
    <div class="btnBoxTop">
      <div class="closeBtn">
        <i class="material-icons-round" @click="close">clear</i>
      </div>
    </div>
    <div class="pageContent scrollable">

    </div>
  </div>
</template>


<script>
import { mapMutations } from 'vuex'
export default {
  methods: {
    ...mapMutations('about', [
      'setShowAboutUs',
    ]),
    close() {
      this.setShowAboutUs(false)
    }
  }
}
</script>

<style lang="scss" scoped>
.outer {
  width: 100%;
  height: 100vh;
  position: absolute;
  top: 0; left: 0;
  z-index: 20;
  background: #EEE;
}
.btnBoxTop {
  width: 100%;
  height: 80px;
  background: #EEE;
  position: relative;
  & > .closeBtn {
    width: 80px;
    height: 80px;
    position: absolute;
    top: 0; right: 0;
    & > i {
      position: absolute;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      color: #AAA;
      font-size: 40px;
      user-select: none;
      cursor: pointer;
    }
  }
}
.pageContent {
  width: 100%;
  height: calc(100% - 80px);
  overflow-y: auto;
}
</style>