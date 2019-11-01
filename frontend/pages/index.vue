<template>
  <div class="index-page"></div>
</template>

<script>
export default {
  components: {},
  created() {
    this.$store.commit('leftSideBar/setDefaultMenu', true)
  }
}
</script>

<style lang="scss" scoped>
.index-page {
  height: 100vh;
  overflow-y: hidden;
}
</style>
