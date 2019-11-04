<template>
  <div class="index-page"></div>
</template>

<script>
export default {
  components: {},
  mounted() {
    this.$store.commit('leftSidebar/setShowDefaultMenu', true)
  }
}
</script>

<style lang="scss" scoped>
.index-page {
  height: 100vh;
  overflow-y: hidden;
}
</style>
