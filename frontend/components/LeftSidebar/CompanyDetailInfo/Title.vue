<template>
  <div class="c-di-t">
    <h1>{{ company.name || '이름' }}</h1>
    <p class="c-di-t-st">
      <span>{{ company.ind_name }}</span>
    </p>
    <hr class="c-di-t-li" />
    <p class="c-di-t-sp">
      신입 평균
      <span>{{ fs }}</span>
    </p>
    <p class="c-di-t-ap">
      직원 평균
      <span>{{ as }}</span>
    </p>
    <p class="c-di-t-time">
      <span class="span-station">{{ station }}역</span>
      에서
      <span class="span-name">{{ company.name }}</span>
      까지 약
      <span class="span-time">{{ transitTime }}</span>
      분 예상
    </p>
    <p class="c-di-t-jc">
      현재 진행중인 채용 공고 개수
      <span>{{ company.jobs_count }} 개</span>
    </p>
    <div v-if="company.jobs_count">
      <Recruitment v-for="(data, idx) in recruitments" :key="data.open + idx" :data="data" />
    </div>
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
  </div>
</template>

//TODO og:image
<script>
import { mapGetters } from 'vuex'
import Recruitment from './recruitment'
export default {
  name: 'Title',
  components: { Recruitment },
  computed: {
    ...mapGetters('company', {
      company: 'getCompanyDetail',
      allCompanies: 'getAllCompanies'
    }),
    ...mapGetters('jobs', {
      recruitments: 'getJobData'
    }),
    ...mapGetters('localStorage', {
      station: 'getDepartureStationName'
    }),
    transitTime() {
      let tt = 0
      this.allCompanies.forEach((c) => {
        if (c.id === this.company.id) {
          tt = c.transitTime
        }
      })
      return tt
    },
    googleRouteLink() {
      let stationName = ''
      if (
        this.station.slice(this.station.length - 1, this.station.length) ===
        '역'
      ) {
        stationName = this.station
      } else {
        stationName = this.station + '역'
      }
      return `https://www.google.com/maps/dir/${stationName}/${this.company.name}/`
    },
    fs() {
      return this.company.start_salary
        ? this.company.start_salary + '만원'
        : '회사내규에 따름'
    },
    as() {
      return this.company.average_salary
        ? this.company.average_salary + '만원'
        : '회사내규에 따름'
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
          hid: 'og:site_name',
          property: 'og:site_name',
          content: `${this.company.name} - 길잡이`
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content: this.company.name
        },
        {
          hid: 'og:description',
          name: 'og:description',
          content: `${this.company.name}에 대한 취업 정보 및 지도와 연봉 정보가 담겨져 있습니다.`
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

.c-di-t-time {
  span {
    font-weight: 700;
  }
}

.span-station {
  color: #9774f1;
}
.span-name {
  color: #8774c1;
}
.span-time {
  color: #4876ef;
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
  background-color: #9794d1;
  padding: 10px;
  border-radius: 5px;
  text-align: center;
  margin-top: 15px !important;
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
    margin-left: 10px;
    font-size: 18px;
    color: #8774c1;
    font-weight: 700;
  }
}

.saramin {
  width: 100%;
  color: #bbb;
  padding: 5px;
  text-align: center;
  font-size: 12px;
  font-weight: 100;
}
</style>
