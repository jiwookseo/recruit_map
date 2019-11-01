<template>
  <section class="company--detail-info-div">
    <Title />
  </section>
</template>

<script>
import api from '../../../api/company.js'
import Title from './Title'
export default {
  name: 'CompanyDetailInfo',
  components: {
    Title
  }
}
</script>

<style lang="scss" scoped>
.company--detail-info-div {
  width: 100%;
  height: 100vh;
}
</style>
