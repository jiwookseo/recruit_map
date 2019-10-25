<template>
  <div class="company--detail-info-shell">
    <CompanyDetailInfo />
  </div>
</template>

<script>
import CompanyDetailInfo from '../../components/LeftSideBar/CompanyDetailInfo'
export default {
  components: {
    CompanyDetailInfo
  },
  created() {
    this.$store.commit('leftSideBar/setDefaultMenu', false)
  }
}
</script>

<style lang="scss">
.company--detail-info-shell {
  position: absolute;
  top: 0;
  left: 0;
  width: 400px;
  height: 100vh;
  background-color: #8774c1;
}
</style>
