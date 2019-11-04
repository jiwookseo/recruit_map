<template>
  <div class="recruitment-div">
    <h2>{{ data.title }}</h2>
    <p class="rc-j">{{ data.job }}</p>
    <p class="rc-a">
      <span>요구학력</span>
      <span>: {{ data.edu_name }}</span>
    </p>
    <p>
      <span>경력</span>
      <span>: {{ workExperience }}</span>
    </p>
    <p>
      <span>채용 시작</span>
      <span>: {{ openTime }}</span>
    </p>
    <p>
      <span>채용 마감</span>
      <span>: {{ closeTime }}</span>
    </p>
    <p>
      <a :href="data.saramin_url" target="_blank">채용공고 바로가기</a>
    </p>
  </div>
</template>

<script>
export default {
  props: {
    data: {
      type: Object,
      required: true,
      default: {}
    }
  },
  computed: {
    workExperience() {
      if (this.data.exp_max !== 0 && this.data.exp_min !== 0) {
        return `${this.data.exp_min}년 ~ ${this.data.exp_max}년`
      } else if (this.data.exp_min === 0 && this.data.exp_max) {
        return `~ ${this.data.exp_max}년`
      } else if (this.data.exp_min && this.data.exp_max === 0) {
        return `${this.data.exp_min}년 이상`
      } else {
        return '경력 무관'
      }
    },
    openTime() {
      const d = new Date(this.data.open)
      return `${d.getFullYear()}년 ${d.getMonth() + 1}월 ${d.getDate()}일`
    },
    closeTime() {
      const d = new Date(this.data.close)
      return `${d.getFullYear()}년 ${d.getMonth() + 1}월 ${d.getDate()}일 까지`
    }
  }
}
</script>

<style lang="scss" scoped>
.recruitment-div {
  border-bottom: 1.4px solid #aaa;
  padding: 10px;
  margin-top: 20px;
  border-radius: 10px;
  background-color: #EAEAEA;
  h2 {
    text-align: center;
    font-size: 18px;
  }
  p {
    margin-top: 5px;
    font-size: 14px;
    span {
      &:first-child {
        display: inline-block;
        min-width: 80px;
      }
    }
    &:last-child {
      display: block;
      text-align: center;
      margin: 15px 0 10px;
      a {
        text-decoration: none;
        text-align: center;
        padding: 5px 10px;
        border-radius: 5px;
        background-color: #8774c1;
        color: #fff;
        cursor: pointer;
      }
    }
  }
}
p.rc-j {
  color: #999;
  font-size: 12px;
}
</style>
