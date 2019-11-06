<template>
  <section>
    <div class="Title">주요 기능 3: 지도 탐방</div>
    <div class="Content">
      <p class="txt1">지도를 드래그하면 주변의 회사 목록이 좌측에 실시간으로 업데이트됩니다.</p>
      <div class="imgBox">
        <img class="navImg" src="~/static/aboutus-f3-navigate.png" alt="">
      </div>
      <br>
      <p class="txt1">검색창에서 특정 회사를 찾아볼 수도 있어요~</p>
      <div class="imgBox">
        <img src="~/static/aboutus-f3-search.png" alt="" class="searchImg">
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Feature3"
}
</script>

<style lang="scss" scoped>
@import '~/assets/aboutus.scss';
.navImg {
  height: 200px;
}
.searchImg {
  height: 150px;
}
</style>