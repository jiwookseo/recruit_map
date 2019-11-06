<template>
  <section>
    <div class="Title">기술 스택</div>
    <div class="Content">
      <p class="txt1">저희 서비스는 다음의 기술들로 완성되었어요:</p>
      <div class="imgBox">
        <img src="~/static/aboutus-tech1.png" alt="">
        <img src="~/static/aboutus-tech2.png" alt="">
        <img src="~/static/aboutus-tech3.png" alt="">
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "TechStack"
}
</script>

<style lang="scss" scoped>
@import '~/assets/aboutus.scss';

img {
  width: 300px;
  margin: 10px 0;
}
</style>