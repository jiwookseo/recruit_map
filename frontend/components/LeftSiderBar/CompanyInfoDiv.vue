<template>
  <section class="company--info-div">
    <article v-for="idx in 5" :key="idx">
      <p>하하힝</p>
    </article>
  </section>
</template>

<script>
export default {
  name: 'CompanyInfoDiv'
}
</script>

<style lang="scss" scoped>
.company--info-div {
  position: absolute;
  top: 70px;
  width: 100%;
  article {
    box-sizing: border-box;
    width: 100%;
    height: 90px;
    background-color: #fff;
    border-bottom: 2px solid #ddd;
    padding: 15px 0 0 15px;
    cursor: pointer;
    &:hover {
      background-color: #aaa;
    }
  }
}
</style>
