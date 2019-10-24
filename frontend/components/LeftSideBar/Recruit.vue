<template>
  <section class="recruit--div">
    <!-- for 문을 돌 때, Recommended Recruit의 length에 맞게 돌게하고,
    Button Slider로 하면 좋을거 같음 + 구현 후 자동으로 슬라이딩 되는 것 까지-->
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
