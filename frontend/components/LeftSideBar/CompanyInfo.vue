<template>
  <!-- 5개의 회사 정보를 보여주는 것에 최적화 되어 있읍니다. -->
  <section class="company--info-div">
    <nuxt-link
      v-for="item in calData"
      :key="item.id + item.avg_salary"
      :to="`/company/${item.id}/`"
    >
      <article @mouseenter="handleMouseEnter(item)" @mouseleave="setShowInfoWindow(false)">
        <p>
          <span class="company-info-name">{{ item.name }}</span>
          <span class="company-info-salary">
            {{
            item.start_salary ? item.start_salary + '만원' : '회사내규에 따름'
            }}
          </span>
        </p>
        <p class="company--info-sub">{{ item.address }}</p>
      </article>
    </nuxt-link>
  </section>
</template>

<script>
import { mapMutations, mapGetters } from 'vuex'
export default {
  name: 'CompanyInfo',
  data() {
    return {
      a: ''
    }
  },
  computed: {
    ...mapGetters('company', [
      'getHoveredCompany',
      'getSelectedCompany',
      'getAllCompanies'
    ]),
    ...mapGetters('maps', ['getLatLng']),
    companiesData() {
      return this.getAllCompanies.slice(0, 5)
    },
    calData() {
      const companyArray = this.getAllCompanies.filter(
        (v) =>
          v.lat >= this.getLatLng[0].lat &&
          v.lat <= this.getLatLng[1].lat &&
          v.lng >= this.getLatLng[0].lng &&
          v.lng <= this.getLatLng[1].lng
      )
      if (companyArray.length > 5) {
        return companyArray.splice(0, 5)
      }
      return companyArray
    }
  },
  methods: {
    ...mapMutations('company', ['setHoveredCompany', 'setSelectedCompany']),
    ...mapMutations('infoWindow', [
      'setInfoWindowPosition',
      'setInfoWindowOptionsContent',
      'setShowInfoWindow'
    ]),
    handleMouseEnter(payload) {
      this.setHoveredCompany(payload)
      this.setInfoWindowPosition({ lat: payload.lat, lng: payload.lng })
      this.setInfoWindowOptionsContent({
        name: payload.name,
        time: payload.transitTime,
        salary: payload.avg_salary,
        jobs: payload.jobs_count
      })
      this.setShowInfoWindow(true)
    }
  }
}
</script>

<style lang="scss" scoped>
.company--info-div {
  position: absolute;
  top: 120px;
  width: 100%;
  border-radius: 2px;
  overflow: hidden;
  a {
    text-decoration: none;
  }
  article {
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-sizing: border-box;
    height: 90px;
    background-color: #fff;
    padding: 5px 15px 5px 15px;
    border-bottom: 1px solid #aaa;
    cursor: pointer;
    &:hover {
      background-color: #ddd;
    }
    p {
      color: #181818;
    }
    &:last-child {
      border: none;
    }
  }
}

.company-info-name {
  font-weight: 600;
  font-size: 16px;
}

.company-info-salary {
  display: inline-block;
  font-size: 13px;
  background-color: rebeccapurple;
  color: #fff;
  padding: 5px 10px;
  border-radius: 3px;
}

.company--info-link {
  display: inline-block;
  font-size: 13px;
  background-color: #18186f;
  color: #fff;
  padding: 5px 10px;
  border-radius: 3px;
  text-decoration: none;
}

.company--info-sub {
  font-size: 14px;
  margin-top: 3px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
