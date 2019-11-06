<template>
  <section
    class="recruit--div"
    @mouseenter="hoverAds = true"
    @mouseleave="hoverAds = false"
  >
    <!-- for 문을 돌 때, Recommended Recruit의 length에 맞게 돌게하고,
    Button Slider로 하면 좋을거 같음 + 구현 후 자동으로 슬라이딩 되는 것 까지-->
    <div class="ad" v-for="ad in ads" :key="ad.id">
      <a v-if="ad.type==='link'" :href="ad.url" target="_blank" :title="ad.name">
        <article :style="{ backgroundImage: `url(${imgUrl(ad.img)})` }" />
      </a>
      <div v-if="ad.type==='button'" class="buttonType">
        <img :src="imgUrl(ad.img)" :alt="ad.name" @click="clickHandler(ad.action)">
      </div>
    </div>
    <div class="btnContainer left">
      <div class="btn left" :class="{ hide: !hoverAds }">
        <i class="material-icons-round">keyboard_arrow_left</i>
      </div>
    </div>
    <div class="btnContainer right">
      <div class="btn right" :class="{ hide: !hoverAds }">
        <i class="material-icons-round">keyboard_arrow_right</i>
      </div>
    </div>
  </section>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  name: 'Recruit',
  data() {
    return {
      hoverAds: false,
      ads: [
        {
          id: 1,
          type: 'link',
          name: 'SSAFY 3기 모집',
          url: 'https://www.ssafy.com/ksp/jsp/swp/swpMain.jsp',
          img: 'ad-s3.png'
        },
        {
          id: 2,
          type: 'button',
          name: 'About Us',
          action: 'openAboutUs',
          img: 'ad-aboutus.png'
        },
        {
          id: 3,
          type: 'link',
          name: 'HogangNono',
          url: 'https://hogangnono.com/',
          img: 'ad-hogang.png'
        },
        {
          id: 4,
          type: 'button',
          name: '광고문의',
          action: '',
          img: 'ad.png'
        }
      ]
    }
  },
  methods: {
    ...mapMutations('about', [
      'setShowAboutUs',
    ]),
    imgUrl: (fn) => {
      return require(`../../static/${fn}`)
    },
    clickHandler(action) {
      if (action === "openAboutUs") {
        this.setShowAboutUs(true)
      }
    }
  },
  mounted() {
    $(document).ready(function() {
      $('.ad')
        .eq(0)
        .css({
          left: 0
        })

      let i = 0
      const count = $('.ad').length
      const slidetime = 700
      const intervaltime = 10000
      let slideshow

      function btn_init() {
        $('.btn.right').css('pointer-events', 'none')
        $('.btn.left').css('pointer-events', 'none')
        setTimeout(function() {
          $('.btn.right').css('pointer-events', '')
          $('.btn.left').css('pointer-events', '')
        }, slidetime)
      }
      function adSlide(s_out, pos1, s_in, pos2) {
        $('.ad')
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

        $('.ad')
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
      $('.btn.right').click(function() {
        btn_init()
        right()
      })
      $('.btn.left').click(function() {
        btn_init()
        left()
      })
      $('.recruit--div').mouseenter(function(){
        stop();
      });
      $('.recruit--div').mouseleave(function(){
        start();
      });
      start();
    })
  },
}
</script>

<style lang="scss" scoped>
.recruit--div {
  position: absolute;
  bottom: 0;
  left: 0;
  display: flex;
  border-radius: 2px;
  width: 100%;
  height: 140px;
  overflow: hidden;
  background: #FFF;
  & > .ad {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: -100%;
    cursor: pointer;
  }
  a,
  article {
    width: 100%;
    height: 100%;
    overflow: hidden;
  }
  article {
    background-color: white;
    background-position: center;
    background-size: cover;
  }
  .btnContainer {
    width: 30px;
    height: 100%;
    position: absolute;
    top: 0;
    &.left {
      left: 0;
    }
    &.right {
      right: 0;
    }
  }
  .btn {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    cursor: pointer;
    transition: all 0.3s;
    i {
      font-size: 40px;
      text-shadow: 0 0 2px #aaa;
      position: relative;
      transform: translateY(2px);
    }
    &.hide {
      display: none;
    }
  }
}
.buttonType {
  width: 100%; height: 100%;
  & > img {
    width: 100%; height: 100%;
    object-fit: cover;
  }
}
</style>
