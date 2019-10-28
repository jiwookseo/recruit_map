<template>
  <section class="company--detial-info-div">
    <Title />
  </section>
</template>

<script>
import Title from './Title'
import api from '../../../api/company.js'
export default {
  name: 'CompanyDetailInfo',
  components: {
    Title
  },
  mounted() {
    let data = api.getCompanyData(this.$route.params.id)
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
