<template>
  <!-- 5개의 회사 정보를 보여주는 것에 최적화 되어 있읍니다. -->
  <section class="company--info-div">
    <nuxt-link
      v-for="item in calData"
      :key="item.id + item.avg_salary"
      :to="`/company/${item.id}/`"
      class="company-item"
    >
      <article @mouseenter="handleMouseEnter(item)" @mouseleave="setShowInfoWindow(false)">
        <p>
          <span class="company-info-name">{{ item.name }}</span>
          <span class="company-info-salary">
            {{
            item.avg_salary ? item.avg_salary + '만원' : '회사내규에 따름'
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
    ...mapGetters('localStorage', ['getFilteredCompanies']),
    ...mapGetters('maps', ['getLatLng']),
    companiesData() {
      const data =
        this.getFilteredCompanies.length >= 1
          ? this.getFilteredCompanies
          : this.getAllCompanies
      return data.slice(0, 5)
    },
    calData() {
      const data =
        this.getFilteredCompanies.length >= 1
          ? this.getFilteredCompanies
          : this.getAllCompanies
      const companyArray = data.filter(
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
  top: 105px;
  width: 100%;
  max-height: calc(100% - 105px - 150px);
  border-radius: 2px;
  overflow-y: auto;
  background: #FFF;
  &::-webkit-scrollbar {
    display: initial;
    width: 7px;
    box-shadow: inset 0 0 1px rgba(0, 0, 0, 0.1);
    border-radius: 50px;
    -webkit-border-radius: 50px;
    &:hover {
      box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.15);
    }
  }
  &::-webkit-scrollbar-thumb:vertical {
    border-radius: 50px;
    -webkit-border-radius: 50px;
    background-color: rgba(0, 0, 0, 0.2);
    background-clip: padding-box;
    border: 1px solid rgba(0, 0, 0, 0);
    min-height: 10px;
    &:active {
      background-color: rgba(0, 0, 0, 0.3);
      border-radius: 50px;
      -webkit-border-radius: 50px;
    }
  }
  a.company-item {
    text-decoration: none;
    display: inline-block;
    width: 100%;
    height: 90px;
    background-color: #fff;
    border-bottom: 1px solid #CCC;
    &:last-child {
      border: none;
    }
    &:hover {
      background-color: #EEE;
    }
  }
  article {
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-sizing: border-box;
    height: 100%;
    padding: 5px 15px 5px 15px;
    cursor: pointer;
    p {
      color: #181818;
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
  padding: 4px 8px;
  border-radius: 2px;
  margin-left: 5px;
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
