<template>
  <section>
    <div class="Title">주요 기능 1: 전체보기 vs 상세보기</div>
    <div class="Content">
      <p class="txt1">전체보기: 출퇴근 시간과 연봉을 한눈에 파악해요~</p>
      <div class="imgBox">
        <img class="overviewImg" src="https://i.imgur.com/pIHqf7i.png" alt="">
      </div>
      <br>
      <p class="txt2">지도에 표시된 마커 모양과 색상으로 대략적인 연봉 및 출퇴근 시간 수준을 알 수 있습니다.</p>
      <div class="markerDesc">
        <div class="markerRow">
          <div class="marker">
            <img src="https://i.imgur.com/9EMDLEC.png" alt="">
            <p class="label">30분 이내</p>
          </div>
          <div class="marker">
            <img src="https://i.imgur.com/zEAWAej.png" alt="">
            <p class="label">45분 이내</p>
          </div>
          <div class="marker">
            <img src="https://i.imgur.com/YrEPYUO.png" alt="">
            <p class="label">60분 이내</p>
          </div>
          <div class="marker">
            <img src="https://i.imgur.com/8gUciAP.png" alt="">
            <p class="label">60분 초과</p>
          </div>
        </div>
        <div class="markerRow">
          <div class="marker">
            <img src="https://i.imgur.com/8gUciAP.png" alt="">
            <p class="label">연봉 4000 미만</p>
          </div>
          <div class="marker">
            <img src="https://i.imgur.com/MGIH1Pi.png" alt="">
            <p class="label">연봉 4000 이상</p>
          </div>
          <div class="marker">
            <img src="https://i.imgur.com/UNqHYfQ.png" alt="">
            <p class="label">연봉 5000 이상</p>
          </div>
        </div>
        <div class="markerRow">
          <div class="marker">
            <img src="https://i.imgur.com/5VcItZX.png" alt="">
            <p class="label">현재 채용 중인 공고 없음</p>
          </div>
        </div>
      </div>
      <br>
      <br>
      <br>
      <p class="txt1">상세보기: 회사의 상세 정보까지 확인해요~</p>
      <p class="txt2">관심 있는 회사의 마커를 클릭하면 좌측에 회사 상세 정보가 뜹니다.</p>
      <div class="imgBox">
        <img class="detailImg" src="https://i.imgur.com/tkM85n9.png" alt="">
      </div>
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

.overviewImg {
  height: 200px;
}
.detailImg {
  height: 300px;
}
.markerRow {
  display: flex;
  justify-content: space-evenly;
  padding: 10px 0;
  border-bottom: 1px solid #CCC;
  &:last-child {
    border: none;
  }
  .marker {
    img {
      width: 80px;
      display: inline-block;
    }
    .label {
      font-size: 12px;
    }
  }
}



</style>