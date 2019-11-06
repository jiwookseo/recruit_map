<template>
  <section>
    <div class="Title">팀원 소개</div>
    <div class="Content">
      <div class="Container">
        <div class="Card" v-for="m in members" :key="m.id">
          <div class="profImg">
            <img :src="m.profImg" alt="">
          </div>
          <div class="nameBox">
            <div class="name">{{m.name}}</div>
            <div class="github">
              <a :href="m.gitHub" target="_blank">
                <img :src="require('~/static/github-logo.svg')" alt="GitHub">
              </a>
            </div>
          </div>
          <div class="role">
            {{m.role}}
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Members",
  data: () => ({
    members: [
      {
        id: 1,
        name: '김도우',
        profImg: "https://avatars2.githubusercontent.com/u/41623836?s=460&v=4",
        gitHub: "https://github.com/dowookims",
        role: "팀장 | 프론트엔드"
      },
      {
        id: 2,
        name: '서지욱',
        profImg: "https://avatars1.githubusercontent.com/u/30630564?s=460&v=4",
        gitHub: "https://github.com/jiwookseo",
        role: "백엔드"
      },
      {
        id: 3,
        name: '윤지원',
        profImg: "https://avatars1.githubusercontent.com/u/45954965?s=460&v=4",
        gitHub: "https://github.com/jiwonjulietyoon",
        role: "프론트엔드"
      }
    ]
  })
}
</script>

<style lang="scss" scoped>
@import '~/assets/aboutus.scss';

.Content {
  position: relative;
}

.Container {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 100%;
  display: flex;
  justify-content: space-between !important;
  align-items: flex-end;
}
.Card {
  width: 200px;
  height: 350px;
  .profImg {
    width: 160px;
    height: 160px;
    margin: 20px;
    img {
      width: 100%; height: 100%;
      object-fit: cover;
    }
  }
  .nameBox {
    width: 140px;
    height: 50px;
    margin-left: 30px;
    position: relative;
    font-size: 25px;
    font-weight: bold;
    .github {
      width: 30px;
      height: 30px;
      position: absolute;
      right: 10px;
      top: 5px;
      a, img {
        width: 100%; height: 100%;
      }
    }
  }
  .role {
    width: 140px;
    margin-left: 30px;
  }
}
</style>