<template>
  <div class="c-di-t">
    <h1>{{company.name || '이름'}}</h1>
    <p class="c-di-t-st">
      <span>{{ company.ind_name }}</span>
      <span>신입 {{company.start_salary}}</span>
      <span>평균 {{company.avg_salary}}</span>
    </p>
    <p>
      <span>회사홈페이지 :</span>
      <a target="_blank" :href="company.href">{{company.href}}</a>
    </p>
    <p>
      <a target="_blank" :href="company.saramin_url">
        <span>채용 공고 바로 가기</span>
      </a>
    </p>
    <p>
      현재 진행중인 채용 공고 개수
      <span>{{company.jobs_count}}</span>
    </p>
    <p>
      <span>power by saram in</span>
    </p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Title',
  computed: {
    ...mapGetters('company', {
      company: 'getACompanyDetailInfo'
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
}
</style>
