<template>
  <div class="c-di-t">
    <h1>{{ company.name || '이름' }}</h1>
    <p class="c-di-t-st">
      <span>{{ company.ind_name }}</span>
    </p>
    <hr class="c-di-t-li" />
    <p class="c-di-t-sp">
      신입 평균
      <span>{{ company.start_salary }} 만원</span>
    </p>
    <p class="c-di-t-ap">
      직원 평균
      <span>{{ company.avg_salary }} 만원</span>
    </p>
    <p class="c-di-t-jc">
      현재 진행중인 채용 공고 개수
      <span>{{ company.jobs_count }}</span>
    </p>
    <Recruitment v-for="(data, idx) in recruitments" :key="data.open + idx" :data="data" />
    <p class="c-di-t-cp">
      <a target="_blank" :href="company.href">회사홈페이지 바로 가기</a>
    </p>
    <p class="c-di-t-rp">
      <a target="_blank" :href="company.saramin_url">
        <span>채용 공고 바로 가기</span>
      </a>
    </p>
    <p class="c-di-t-gr">
      <a target="_blank" :href="googleRouteLink">
        <span>구글맵에서 경로 보기</span>
      </a>
    </p>
    <p class="saramin">
      <span>powered by saramin</span>
    </p>
    <div class="back">
      <nuxt-link to="/">
        <i class="material-icons-round">arrow_left_alt</i>
      </nuxt-link>
    </div>
    <!-- 추가적으로 해야 할 것 ! company/:pk/jobs -->
  </div>
</template>

//TODO og:image
<script>
import Recruitment from './recruitment'
import { mapGetters } from 'vuex'
export default {
  name: 'Title',
  components: { Recruitment },
  computed: {
    ...mapGetters('company', {
      company: 'getCompanyDetail'
    }),
    ...mapGetters('jobs', {
      recruitments: 'getJobData'
    }),
    ...mapGetters('localStorage', {
      station: 'getDepartureStationName'
    }),
    googleRouteLink() {
      return `https://www.google.com/maps/dir/${this.station}/${this.company.name}/`
    }
  },
  head() {
    return {
      title: this.company.name,
      meta: [
        {
          hid: 'description',
          property: 'description',
          content: this.company.name
        },
        {
          hid: 'keywords',
          name: 'keywords',
          content: `${this.company.name} ${this.company.name}채용 ${this.company.name}연봉 ${this.company.name}거리`
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content: this.company.name
        },
        {
          hid: 'og:description',
          name: 'og:description',
          content: this.company.name
        }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
.c-di-t {
  top: 70px;
  width: 100%;
  position: absolute;
  display: flex;
  flex-direction: column;
  padding: 20px;
  background-color: #f7f7f7;
  z-index: 9;
  h1 {
    font-weight: 700;
    margin-left: 30px;
    display: inline-block;
    width: calc(100%-40px);
  }
  a {
    text-decoration: none;
    color: #181818;
  }
  p {
    margin-top: 7px;
  }
}

.back {
  position: absolute;
  display: flex;
  top: 2px;
  font-weight: 700;
  left: -10px;
  i {
    font-size: 70px;
    color: #181818;
  }
}

.c-di-t-st {
  margin-top: 4px !important;
  font-size: 12px;
  color: #aaa;
}

.c-di-t-li {
  margin-top: 5px;
}
.c-di-t-sp,
.c-di-t-ap {
  display: inline-block;
  span {
    padding: 5px 10px;
    font-size: 20px;
    font-weight: 600;
  }
}
.c-di-t-rp,
.c-di-t-cp,
.c-di-t-gr {
  width: 100%;
  background-color: #4876ef;
  padding: 10px;
  border-radius: 5px;
  text-align: center;
  a {
    color: #fff;
  }
}

.c-di-t-cp {
  background-color: #181818;
  color: #fff;
}

.c-di-t-gr {
  background-color: #37aa56;
}

.c-di-t-jc {
  span {
    color: #8774c1;
    font-size: 20px;
    font-weight: 550;
  }
}

.saramin {
  width: 35%;
  color: #bbb;
  padding: 5px;
  text-align: center;
  font-size: 12px;
  font-weight: 100;
}
</style>
