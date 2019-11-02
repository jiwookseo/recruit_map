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
  overflow-y: scroll;
  &::-webkit-scrollbar {
    width: 10px;
  }

  /* Track */
  &::-webkit-scrollbar-track {
    background: #8774c1;
  }

  /* Handle */
  &::-webkit-scrollbar-thumb {
    background: #5744c1;
    border-radius: 10px;
  }

  /* Handle on hover */
  &::-webkit-scrollbar-thumb:hover {
    background: #555;
  }
}
</style>
