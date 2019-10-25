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
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Title',
  computed: {
    ...mapGetters('company', {
      company: 'getCompanyDetail'
    })
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
  background-color: #fafafa;
  z-index: 100;
  h1 {
    font-weight: 500;
  }
  a {
    text-decoration: none;
    color: #181818;
  }
  p {
    margin-top: 15px;
  }
}

.c-di-t-st {
  margin-top: 4px !important;
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
  background-color: #4876ef;
  color: #fff;
  padding: 5px;
  text-align: center;
  font-size: 12px;
}
</style>
