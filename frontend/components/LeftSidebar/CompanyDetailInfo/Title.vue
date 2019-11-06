<template>
  <div class="c-di-t">
    <div class="fixed">
      <div class="c-name-row">
        <h1 class="c-name">
          {{ company.name || '이름' }}
          <a target="_blank" :href="company.href" title="홈페이지 바로가기">
            <i class="material-icons-round">exit_to_app</i>
          </a>
        </h1>
      </div>
      <p class="c-di-t-st">
        <span>{{ company.ind_name }}</span>
        <span>{{ company.scale }}</span>
      </p>
      <div class="back" @click.stop="goBack">
        <i class="material-icons-round">arrow_left_alt</i>
      </div>
    </div>
    <div class="scrollable">
      <p class="c-di-t-sp">
        신입 평균
        <span>{{ fs }}</span>
      </p>
      <p class="c-di-t-ap">
        직원 평균
        <span>{{ as }}</span>
      </p>
      <!-- @HOTFIX: line break -->
      <p class="c-di-t-time">
        <span class="span-station">{{ station }}역</span>
        에서
        <span class="span-name">{{ company.name }}</span>
        까지
        <br />약
        <span class="span-time">{{ transitTime }}</span> 분 예상
        <a target="_blank" :href="googleRouteLink">
          <span class="route">길찾기</span>
        </a>
      </p>
      <p class="c-di-t-jc">
        현재 진행중인 채용 공고 개수
        <span>{{ company.jobs_count }} 개</span>
        <a target="_blank" :href="company.saramin_url">공고 보기</a>
      </p>
      <div v-if="company.jobs_count">
        <Recruitment v-for="(data, idx) in recruitments" :key="data.open + idx" :data="data" />
      </div>
      <p class="saramin">
        <span>powered by saramin</span>
      </p>
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
  methods: {
    goBack() {
      this.$router.push('/')
    }
  },
  head() {
    return {
      title: this.company.name,
      meta: [
        {
          property: 'description',
          content: this.company.name
        },
        {
          name: 'keywords',
          content: `${this.company.name} ${this.company.name}채용 ${this.company.name}연봉 ${this.company.name}거리`
        },
        {
          property: 'og:site_name',
          content: `${this.company.name} - 길잡이`
        },
        {
          property: 'og:title',
          content: this.company.name
        },
        {
          property: 'og:description',
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
  height: calc(100% - 70px);
  position: absolute;
  display: flex;
  flex-direction: column;
  background-color: #f7f7f7;
  z-index: 9;
  .fixed {
    padding: 15px;
    border-bottom: 1px solid #aaa;
    box-sizing: border-box;
    position: relative;
  }
  .c-name-row {
    padding-left: 30px;
    position: relative;
    h1.c-name {
      font-weight: 700;
      display: inline-block;
      vertical-align: top;
    }
    a {
      display: inline-block;
      vertical-align: top;
      margin: 5px 0 0 5px;
      width: 30px;
      height: 30px;
      position: relative;
      top: 0px;
      overflow: hidden;
    }
    i {
      font-size: 1.1em;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      color: #181818;
    }
  }
  .c-di-t-st {
    margin-top: 4px !important;
    margin-left: 30px;
    font-size: 12px;
    span {
      color: #aaa;
      &:nth-child(2) {
        margin-left: 5px;
        background-color: rebeccapurple;
        color: #fff;
        padding: 1px 5px 2px;
        border-radius: 15px;
        font-size: 10px;
        position: relative;
        top: -1px;
        user-select: none;
      }
    }
  }
  .back {
    width: 50px;
    height: 50px;
    position: absolute;
    top: 0;
    left: -10px;
    font-weight: 700;
    overflow: hidden;
    a,
    i {
      width: 100%;
      height: 100%;
      display: inline-block;
    }
    i {
      max-width: 50px;
      max-height: 50px;
      font-size: 70px;
      color: #181818;
      cursor: pointer;
    }
  }
}

// SCROLLABLE SECTION
.scrollable {
  overflow-y: auto;
  padding: 15px;
  &::-webkit-scrollbar {
    width: 10px;
  }
  /* Track */
  &::-webkit-scrollbar-track {
    background: #8774c1;
  }
  /* Handle */
  &::-webkit-scrollbar-thumb {
    background: #5744c1;
    border-radius: 10px;
  }
  /* Handle on hover */
  &::-webkit-scrollbar-thumb:hover {
    background: #555;
  }
  p {
    min-height: 25px;
  }
}
.c-di-t-sp,
.c-di-t-ap {
  span {
    margin-left: 10px;
    font-weight: 600;
    font-size: 0.9em;
  }
}
a {
  text-decoration: none;
  color: #181818;
}
p {
  margin-top: 7px;
}

.c-di-t-time {
  span {
    font-weight: 700;
  }

  .span-station,
  .span-name,
  .span-time {
    color: #4876ef;
  }

  a {
    display: inline-block;
  }
  .route {
    display: inline-block;
    padding: 3px 5px 4px;
    color: #fff;
    background: #3766f3;
    font-size: 11px;
    border-radius: 5px;
    margin-left: 5px;
    cursor: pointer;
    position: relative;
    top: -2px;
    letter-spacing: 1px;
    font-weight: 400;
    &:hover {
      background: #2054f3;
    }
  }
}
.c-di-t-jc {
  span {
    margin-left: 3px;
    color: #8774c1;
    font-weight: 700;
  }
  a {
    display: inline-block;
    padding: 3px 5px 4px;
    color: #fff;
    background: #806db8;
    font-size: 11px;
    border-radius: 5px;
    margin-left: 5px;
    cursor: pointer;
    position: relative;
    top: -2px;
    letter-spacing: 1px;
    font-weight: 400;
    &:hover {
      background: #6e5e9e;
    }
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
