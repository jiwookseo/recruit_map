<template>
  <section class="company--detial-info-div">
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
  },
  mounted() {
    const data = api.getCompanyData(this.$route.params.id)
    data
      .then((res) => res.data)
      .then((res) => {
        this.$store.commit('company/setCompanyDetail', res)
      })
  }
}
</script>

<style lang="scss" scoped>
.company--detial-info-div {
  width: 100%;
  height: 100%;
}
</style>
