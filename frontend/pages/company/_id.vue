<template>
  <div class="company--detail-info-shell">
    <CompanyDetailInfo />
  </div>
</template>

<script>
import CompanyDetailInfo from '../../components/LeftSidebar/CompanyDetailInfo'
export default {
  components: {
    CompanyDetailInfo
  },
  created() {
    this.$store.commit('leftSidebar/setShowDefaultMenu', false)
    this.$store.commit('leftSidebar/setShowSearchbar', false)
  }
}
</script>

<style lang="scss">
.company--detail-info-shell {
  position: absolute;
  top: 0;
  left: 0;
  width: 380px;
  height: 100vh;
  background-color: #8774c1;
  overflow: hidden;
  
}
</style>
