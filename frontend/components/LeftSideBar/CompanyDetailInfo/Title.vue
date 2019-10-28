<template>
  <div class="c-di-t">
    <h1>{{company.name || '이름'}}</h1>
    <p class="c-di-t-st">
      <span>{{ company.ind_name }}</span>
    </p>
    <hr class="c-di-t-li" />
    <p class="c-di-t-sp">
      신입 평균
      <span>{{company.start_salary}} 만원</span>
    </p>
    <p class="c-di-t-ap">
      직원 평균
      <span>{{company.avg_salary}} 만원</span>
    </p>
    <p class="c-di-t-cp">
      <a target="_blank" :href="company.href">회사홈페이지 바로 가기</a>
    </p>
    <p class="c-di-t-rp">
      <a target="_blank" :href="company.saramin_url">
        <span>채용 공고 바로 가기</span>
      </a>
    </p>
    <p class="c-di-t-jc">
      현재 진행중인 채용 공고 개수
      <span>{{company.jobs_count}}</span>
    </p>
    <p class="saramin">
      <span>powered by saramin</span>
    </p>
    <div class="back">
      <span>&lt;</span>
    </div>
  </div>
</template>

//TODO og:image
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Title',
  computed: {
    ...mapGetters('company', {
      company: 'getCompanyDetail'
    })
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
  z-index: 100;
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
    margin-top: 15px;
  }
}

.back {
  position: absolute;
  display: flex;
  top: 10px;
  font-weight: 700;
  font-size: 30px;
  color: #181818;
  span {
    padding: 3px;
    max-width: 40px;
    max-height: 30px;
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
  width: 47%;
  display: inline-block;
  span {
    background-color: red;
    padding: 5px 10px;
    color: white;
    border-radius: 5px;
  }
}
.c-di-t-rp,
.c-di-t-cp {
  width: 55%;
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

.c-di-t-jc {
  span {
    color: #181818;
    font-size: 18px;
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
