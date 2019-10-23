<template>
  <section class="recruit--div">
    <article v-for="idx in 5" :key="idx">
      <p>하하하</p>
    </article>
  </section>
</template>

<script>
export default {
  name: 'Recruit'
}
</script>

<style lang="scss">
.recruit--div {
  background-color: #755eb5;
  position: absolute;
  display: flex;
  top: 540px;
  border-radius: 10px;
  padding: 20px 0 0 20px;
  width: 100%;
  height: 140px;
  overflow-x: hidden;
  article {
    min-width: 100%;
    height: 100%;
  }
}
</style>
