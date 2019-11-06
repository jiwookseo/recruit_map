<template>
  <section>
    <div class="Title">주요 기능 2: 나만의 조건 검색</div>
    <div class="Content">
      <p class="txt1">출발 지하철역을 설정해요~</p>
      <p class="txt2">임의로 지정한 지하철역으로부터의 출퇴근 거리를 확인할 수 있습니다.</p>
      <div class="imgBox">
        <img class="departureImg" src="~/static/aboutus-f2-departure.png" alt="">
      </div>
      <br>
      <p class="txt1">연봉, 출퇴근시간, 기업 규모로 필터링해요~</p>
      <div class="imgBox">
        <img class="filterImg" src="~/static/aboutus-f2-filter.png" alt="">
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Feature2"
}
</script>

<style lang="scss" scoped>
@import '~/assets/aboutus.scss';
.departureImg {
  height: 200px;
}
.filterImg {
  height: 150px;
}
</style>