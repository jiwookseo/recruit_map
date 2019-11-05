<template>
  <v-app dark class="app-error-page">
    <div class="outer">
      <div class="inner">
        <div class="mapIcon">
          <div class="map m1">
            <div class="line"></div>
            <div class="ex"></div>
            <div class="ex e2"></div>
          </div>
          <div class="map m2">
            <div class="line l2"></div>
          </div>
          <div class="map m3">
            <div class="line l3"></div>
            <div class="circle"></div>
          </div>
          <div class="markerBox">
            <i class="material-icons-round marker">room</i>
            <i class="material-icons-round marker marker2">room</i>
            <div class="txt">{{ error.statusCode }}</div>
          </div>
        </div>
        <div v-if="error.statusCode === 404" class="errorMsg">잘못된 경로입니다 :(<br>{{secondsLeft}}초 뒤에 메인페이지로 이동합니다.</div>
        <div v-else class="errorMsg">페이지를 표시할 수 없습니다.<br>관리자에게 문의해주세요.</div>
      </div>
    </div>
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
      secondsLeft: 5
    }
  },
  created() {
    if (this.error.statusCode === 404) {
      setTimeout(() => {
        setInterval(() => {
          this.secondsLeft--
        }, 1000);
      }, 100);
      setTimeout(() => {
        this.$router.push('/')
      }, 5000)
    }
  }
}
</script>

<style lang="scss" scoped>
.app-error-page {
  position: absolute;
  left: 0;
  top: 0;
  width: 100vw;
  height: 100vh;
  z-index: 99999999999;
  overflow: hidden;
}
.outer {
  width: 100%;
  height: 100%;
  background: #ddd;
  position: relative;
  .inner {
    width: 90%;
    max-width: 600px;
    height: 500px;
    // border: 1px solid red;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}
.mapIcon {
  width: 350px;
  height: 350px;
  // border: 1px solid cyan;
  margin: 0 auto;
  position: relative;
  perspective: 200px;
  user-select: none;
  .map {
    width: 80px;
    height: 90px;
    position: absolute;
    bottom: 50px;
    background: #7bc449;
    border: 10px solid #fff;
  }
  .m1 {
    transform: rotateX(20deg) skew(5deg, 15deg);
    left: 50px;
    border-right: none;
  }
  .m2 {
    transform: rotateX(20deg) skew(5deg, -15deg);
    left: 130px;
    background: #69a540;
    border-right: none;
    border-left: none;
    border-color: #eee;
  }
  .m3 {
    transform: rotateX(20deg) skew(5deg, 15deg);
    left: 210px;
    border-left: none;
  }
  .line {
    width: 4px;
    height: 90%;
    background: repeating-linear-gradient(to top, crimson, crimson 7px, transparent 7px, transparent 12px);
    position: absolute;
    top: 5px;
    left: 41px;
    transform: rotate(60deg);
    &.l2 {
      height: 110%;
      background: repeating-linear-gradient(to top, rgb(185, 18, 52), rgb(185, 18, 52) 7px, transparent 7px, transparent 12px);
      transform: rotate(-70deg);
      top: -2px;
    }
    &.l3 {
      height: 60%;
      transform: rotate(45deg);
      top: 12px;
      left: 12px;
    }
  }
  .ex {
    width: 4px;
    height: 12px;
    background: crimson;
    position: absolute;
    top: 51px;
    left: 8px;
    border-radius: 2px;
    &.e2 {
      transform: rotate(90deg);
    }
  }
  .circle {
    width: 11px;
    height: 11px;
    border-radius: 50%;
    background: crimson;
    border: 2px solid rgb(185, 18, 52);
    position: absolute;
    top: 8px;
    left: 29px;
  }
  .markerBox {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    animation: bobbing 1s ease-in-out infinite alternate;
  }
  .marker {
    position: absolute;
    top: 80px;
    left: 50%;
    transform: translate(-50%);
    color: rgb(225, 167, 67);
    font-size: 180px;
    &.marker2 {
      top: 88px;
      font-size: 160px;
      color: #efbe67;
    }
  }
  .txt {
    width: 70px;
    height: 50px;
    line-height: 50px;
    text-align: center;
    position: absolute;
    background: #efbe67;
    top: 120px;
    left: 50%;
    transform: translate(-50%);
    color: white;
    font-size: 40px;
    font-weight: bold;
  }
}

@keyframes bobbing {
  0% {transform: translateY(0);}
  100% {transform: translateY(-10px);}
}

.errorMsg {
  height: calc(100% - 350px);
  // border: 1px solid green;
  text-align: center;
  padding-top: 20px;
  color: #181818;
  font-size: 20px;
  white-space: pre-line;
}

h1 {
  font-size: 20px;
}
</style>
