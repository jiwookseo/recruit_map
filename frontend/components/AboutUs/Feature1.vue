<template>
  <section>
    <div class="Title">기능 1: 전체보기 vs 상세보기</div>
    <div class="Content">
      <p class="txt1">전체보기: 출퇴근 시간과 연봉을 한눈에 파악해요~</p>
      <!-- screenshot -->
      <p class="txt2">지도에 표시된 마커 모양과 색상으로 대략적인 연봉 및 출퇴근 시간 수준을 알 수 있습니다.</p>
      <!-- image -->
      <p class="txt1">상세보기: 회사의 상세 정보까지 확인해요~</p>
      <!-- screenshot -->
      <p class="txt2">관심 있는 회사의 마커를 클릭하면 좌측에 회사 상세 정보가 뜹니다.</p>
    </div>
  </section>
</template>

<script>
export default {
  name: "Feature1"
}
</script>

<style lang="scss" scoped>
@import '~/assets/aboutus.scss';
.overview {
  height: 100%;
}
</style>