<template>
  <h1>헬로우 월드</h1>
</template>

<script>
export default {
  created() {
    this.$store.commit('leftSideBar/setDefaultMenu', false)
  }
}
</script>

<style lang="scss">
</style>
