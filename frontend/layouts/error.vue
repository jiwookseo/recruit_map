<template>
  <v-app dark class="app-error-page">
    <h1 v-if="error.statusCode === 404">{{ pageNotFound }}</h1>
    <h1 v-else>{{ otherError }}</h1>
    <NuxtLink to="/">Home page</NuxtLink>
  </v-app>
</template>

<script>
export default {
  layout: 'empty',
  props: {
    error: {
      type: Object,
      default: null
    }
  },
  head() {
    const title =
      this.error.statusCode === 404 ? this.pageNotFound : this.otherError
    return {
      title
    }
  },
  data() {
    return {
      pageNotFound: '404 Not Found',
      otherError: 'An error occurred'
    }
  }
}
</script>

<style scoped>
.app-error-page {
  position: absolute;
  left: 0;
  top: 0;
  width: 100vw;
  height: 100vh;
  z-index: 99999999999;
}
h1 {
  font-size: 20px;
}
</style>
