<template>
  <!-- 5개의 회사 정보를 보여주는 것에 최적화 되어 있읍니다. -->
  <section class="company--info-div">
    <article
      v-for="item in cd"
      :key="item.ind_code + item.avg_salary"
      @mouseenter="handleMouseEnter(item)"
      @mouseleave="setOpen(false)"
    >
      <p>
        <nuxt-link :to="'/place/'+item.ind_code">
          <span class="company-info-name">{{item.name}}</span>
        </nuxt-link>
        <span
          class="company-info-salary"
        >{{item.start_salary ? item.start_salary + '만원' : '회사내규에 따름'}}</span>
        <a target="_blank" class="company--info-link" :href="item.saramin_url">채용링크</a>
      </p>
      <p class="company--info-sub">{{item.address}}</p>
    </article>
  </section>
</template>

<script>
import CD from '../../data_set/company_data'
import { mapMutations, mapGetters } from 'vuex'
export default {
  name: 'CompanyInfo',
  data() {
    return {
      cd: CD.splice(0, 5)
    }
  },
  methods: {
    ...mapMutations('company', ['setHoveredCompany', 'setSelectedCompany']),
    ...mapMutations('infoWindow', [
      'setPosition',
      'setOptionsContent',
      'setOpen'
    ]),
    handleMouseEnter(payload) {
      this.setHoveredCompany(payload)
      this.setPosition({ lat: payload.lat, lng: payload.lng })
      this.setOptionsContent({ name: payload.name, time: payload.avg_salary })
      this.setOpen(true)
    }
  },
  computed: {
    ...mapGetters('company', ['hoveredCompany', 'selectedCompany'])
  }
}
</script>

<style lang="scss" scoped>
.company--info-div {
  position: absolute;
  top: 70px;
  width: 100%;
  article {
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-sizing: border-box;
    width: 100%;
    height: 90px;
    background-color: #fff;
    border-bottom: 2px solid #ddd;
    padding: 5px 15px 0 15px;
    cursor: pointer;
    &:hover {
      background-color: #aaa;
    }
    p {
      a:first-child {
        color: #181818;
      }
    }
  }
}

.company-info-name {
  font-weight: 600;
  font-size: 16px;
}

.company-info-salary {
  display: inline-block;
  font-size: 14px;
  background-color: rebeccapurple;
  color: #fff;
  padding: 5px 10px;
  border-radius: 5px;
}

.company--info-link {
  display: inline-block;
  font-size: 14px;
  background-color: #18186f;
  color: #fff;
  padding: 5px 10px;
  border-radius: 5px;
  text-decoration: none;
}

.company--info-sub {
  font-size: 14px;
}
</style>
