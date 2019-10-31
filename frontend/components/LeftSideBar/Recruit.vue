<template>
  <section class="recruit--div">
    <!-- for 문을 돌 때, Recommended Recruit의 length에 맞게 돌게하고,
    Button Slider로 하면 좋을거 같음 + 구현 후 자동으로 슬라이딩 되는 것 까지-->
    <a :href="ad.url" target="_blank">
      <article />
    </a>
  </section>
</template>

<script>
export default {
  name: 'Recruit',
  data() {
    return {
      ad: {
        id: 'ssafy3',
        name: 'ssafy',
        url: 'https://www.ssafy.com/ksp/jsp/swp/swpMain.jsp'
      }
    }
  }
}
</script>

<style lang="scss">
.recruit--div {
  background-color: #755eb5;
  position: absolute;
  display: flex;
  top: 540px;
  border-radius: 10px;
  width: 100%;
  height: 140px;
  overflow-x: hidden;
  a {
    min-width: 100%;
    min-height: 100%;
  }
  article {
    min-width: 100%;
    min-height: 100%;
    &:first-child {
      background-image: url('../../static/s3.png');
      background-size: 380px 140px;
    }
  }
}
</style>
