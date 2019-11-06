<template>
  <div class="outer">
    <div class="btnBoxTop">
      <div class="closeBtn">
        <i class="material-icons-round" @click="close">clear</i>
      </div>
    </div>
    <div class="pageContentOuter">
      <div class="pageContainerInner">
        <div class="pageContainer">
          <Intro class="page" />
          <Feature1 class="page" />
          <Feature2 class="page" />
          <Feature3 class="page" />
          <TechStack class="page" />
          <Members class="page" />
        </div>
        <div class="btnBox prev">
          <div class="aboutusBtn prev">
            <i class="material-icons-round">keyboard_arrow_left</i>
          </div>
        </div>
        <div class="btnBox next">
          <div class="aboutusBtn next">
            <i class="material-icons-round">keyboard_arrow_right</i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { mapMutations } from 'vuex'
import Intro from '~/components/AboutUs/Intro'
import Feature1 from '~/components/AboutUs/Feature1'
import Feature2 from '~/components/AboutUs/Feature2'
import Feature3 from '~/components/AboutUs/Feature3'
import TechStack from '~/components/AboutUs/TechStack'
import Members from '~/components/AboutUs/Members'

export default {
  components: {
    Intro,
    Feature1,
    Feature2,
    Feature3,
    TechStack,
    Members
  },
  methods: {
    ...mapMutations('about', [
      'setShowAboutUs',
    ]),
    close() {
      this.setShowAboutUs(false)
    }
  },
  mounted() {
    $(document).ready(function() {
      $('.page')
        .eq(0)
        .css({
          left: 0
        })

      let i = 0
      const count = $('.page').length
      const slidetime = 700
      const intervaltime = 8000
      let slideshow

      function btn_init() {
        $('.aboutusBtn.next').css('pointer-events', 'none')
        $('.aboutusBtn.prev').css('pointer-events', 'none')
        setTimeout(function() {
          $('.aboutusBtn.next').css('pointer-events', '')
          $('.aboutusBtn.prev').css('pointer-events', '')
        }, slidetime)
      }
      function adSlide(s_out, pos1, s_in, pos2) {
        $('.page')
          .eq(s_in)
          .css({
            left: pos2
          })
          .animate(
            {
              left: 0
            },
            slidetime
          )

        $('.page')
          .eq(s_out)
          .animate(
            {
              left: pos1
            },
            slidetime
          )
      }
      function right() {
        adSlide(i % count, '-100%', (i + 1) % count, '100%')
        i++
      }
      function left() {
        adSlide(i % count, '100%', (i - 1) % count, '-100%')
        i--
      }
      function start() {
        stop()
        slideshow = setInterval(function() {
          right()
        }, intervaltime)
      }
      function stop() {
        clearInterval(slideshow)
      }
      $('.aboutusBtn.next').click(function() {
        btn_init()
        right()
      })
      $('.aboutusBtn.prev').click(function() {
        btn_init()
        left()
      })
    })
  },
}
</script>

<style lang="scss" scoped>
.outer {
  width: 100%;
  height: 100vh;
  position: absolute;
  top: 0; left: 0;
  z-index: 20;
  background: #EEE;
}
.btnBoxTop {
  width: 100%;
  height: 80px;
  background: #EEE;
  position: relative;
  & > .closeBtn {
    width: 80px;
    height: 80px;
    position: absolute;
    top: 0; right: 0;
    & > i {
      position: absolute;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      color: #AAA;
      font-size: 40px;
      user-select: none;
      cursor: pointer;
    }
  }
}
.pageContentOuter {
  width: 100%;
  height: calc(100% - 80px);
  overflow: auto;
  // border: 1px solid red;
  position: relative;
  &::-webkit-scrollbar {
    display: initial;
    width: 7px;
    box-shadow: inset 0 0 1px rgba(0, 0, 0, 0.1);
    border-radius: 50px;
    -webkit-border-radius: 50px;
    &:hover {
      box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.15);
    }
  }
  &::-webkit-scrollbar-thumb:vertical, 
  &::-webkit-scrollbar-thumb:horizontal {
    border-radius: 50px;
    -webkit-border-radius: 50px;
    background-color: rgba(0, 0, 0, 0.4);
    background-clip: padding-box;
    border: 1px solid rgba(0, 0, 0, 0);
    min-height: 10px;
    &:active {
      background-color: rgba(0, 0, 0, 0.6);
      border-radius: 50px;
      -webkit-border-radius: 50px;
    }
  }
  .pageContainerInner {
    width: 90%;
    max-width: 800px;
    min-width: 400px;
    height: 90%;
    min-height: 500px;
    // border: 1px solid blue;
    position: absolute;
    top: 0; left: 50%;
    transform: translate(-50%);
    .pageContainer {
      width: calc(100% - 100px);
      height: 100%;
      position: absolute;
      top: 0;
      left: 50px;
      // border: 1px solid cyan;
      overflow: hidden;
      .page {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 100%;
        background: #FEFEFE;
        border-radius: 10px;
        padding: 10px;
      }
    }
    .btnBox {
      width: 50px;
      height: 100%;
      position: absolute;
      top: 0;
      // border: 1px solid hotpink;
      &.prev {
        left: 0;
        &:hover {
          animation: bobLeft 0.7s ease-in-out 4 alternate;
        }
      }
      &.next {
        right: 0;
        &:hover {
          animation: bobRight 0.7s ease-in-out 4 alternate;
        }
      }
      .aboutusBtn {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 100%;
        height: 50px;
        overflow: hidden;
        i {
          position: absolute;
          top: 50%; left: 50%;
          transform: translate(-50%, -50%);
          user-select: none;
          cursor: pointer;
          color: #FFF;
          text-shadow: 0 0 2px #aaa;
          font-size: 70px;
        }
      }
    }
  }
}

@keyframes bobRight {
  0% {transform: translateX(0);}
  100% {transform: translateX(5px);}
}
@keyframes bobLeft {
  0% {transform: translateX(0);}
  100% {transform: translateX(-5px);}
}
</style>