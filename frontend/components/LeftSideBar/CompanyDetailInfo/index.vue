<template>
  <section class="company--detail-info-div">
    <Title />
  </section>
</template>

<script>
import Title from './Title'
export default {
  name: 'CompanyDetailInfo',
  components: {
    Title
  },
  mounted() {
    this.$store.dispatch('company/setAsyncCompanyDetail', this.$route.params.id)
  }
}
</script>

<style lang="scss" scoped>
.company--detail-info-div {
  width: 100%;
  height: 100vh;
}
</style>
