<template>
  <div></div>
</template>

<script>
export default {
  components: {},
  created() {
    this.$store.commit('leftSideBar/setDefaultMenu', true)
  }
}
</script>
