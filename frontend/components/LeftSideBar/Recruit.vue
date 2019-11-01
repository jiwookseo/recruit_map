<template>
  <section class="recruit--div">
    <!-- for 문을 돌 때, Recommended Recruit의 length에 맞게 돌게하고,
    Button Slider로 하면 좋을거 같음 + 구현 후 자동으로 슬라이딩 되는 것 까지-->
    <div v-for="ad in ads" :key="ad.id">
      <a :href="ad.url" target="_blank">
        <article :style="{backgroundImage: `url(${imgUrl(ad.img)})`}" />
      </a>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Recruit',
  data() {
    return {
      ads: [
        {
          id: 'ssafy3',
          name: 'ssafy',
          url: 'https://www.ssafy.com/ksp/jsp/swp/swpMain.jsp',
          img: 's3.png'
        },
        {
          id: 'adz',
          name: 'add',
          url: 'jiwonjulietyoon@gmail.com',
          img: 'ad.png'
        }
      ]
    }
  },
  methods: {
    imgUrl: (fn) => {
      return require(`../../static/${fn}`)
    }
  }
}
</script>

<style lang="scss">
.recruit--div {
  position: absolute;
  display: flex;
  top: 540px;
  border-radius: 10px;
  width: 100%;
  height: 140px;
  overflow-x: hidden;
  a {
    min-width: 380px;
    min-height: 140px;
  }
  article {
    min-width: 380px;
    min-height: 140px;
    background-size: 380px 140px;
  }
}
</style>
