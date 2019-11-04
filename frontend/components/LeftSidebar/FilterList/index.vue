<template>
  <div class="filter-list">
    <div class="filter-items">
      <div
        v-for="(menuItem, i) in menuController"
        :key="menuItem.id"
        class="filter-item"
        @click="handleMenu(i)"
      >
        <span>{{ menuItem.name }}</span>
      </div>
    </div>
    <div v-show="menuController[3].active" class="filter-detail">
      <div v-show="menuController[0].active" class="filter-detail-salary">
        <input v-model="filterSalary" type="range" min="0" max="6000" value="0" step="100" />
        <p>{{ filterSalary }} 만원</p>
      </div>
      <div v-show="menuController[1].active" class="filter-detail-time">
        <input v-model="filterTime" type="range" min="15" max="90" value="15" step="15" />
        <p>{{ filterTime >= 90 ? '90분 이상' : filterTime + '분 이내' }}</p>
      </div>
      <div v-show="menuController[2].active" class="filter-detail-size">
        <!-- { major: '대기업', affiliate:'대기업 계열사·자회사', venture: '벤처기업', midSize: '중견기업', smallSize:'중소기업'}  -->
        <div v-for="(item, idx) in filterSize" :key="item.id" class="filter-detail-size-item">
          <input
            :id="item.size"
            v-model="filterSize[idx].active"
            type="checkbox"
            :value="item.size"
            :checked="item.active"
          />
          <i
            class="material-icons-round"
            v-if="filterSize[idx].active"
            @click="handleToggle(idx)"
          >check_box</i>
          <i class="material-icons-round" v-else @click="handleToggle(idx)">check_box_outline_blank</i>
          <label :for="item.size">{{ item.name }}</label>
        </div>
      </div>
      <div v-show="menuController[3].active" class="filter-bottom">
        <div class="filter-recruiting">
          <input
            id="recruiting"
            v-model="filterRecruiting"
            type="checkbox"
            value="recruiting"
            :checked="filterRecruiting"
          />
          <i
            class="material-icons-round"
            v-if="filterRecruiting"
            @click="handleRecruiting"
          >check_box</i>
          <i class="material-icons-round" v-else @click="handleRecruiting">check_box_outline_blank</i>
          <label for="recruiting">현재 채용중인 공고만 보기</label>
        </div>
        <button @click="handleFilter">적용하기</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
export default {
  name: 'FilterList',
  data() {
    return {
      menuController: [
        {
          id: 'm1',
          name: '연봉',
          active: false
        },
        {
          id: 'm2',
          name: '시간',
          active: false
        },
        {
          id: 'm3',
          name: '규모',
          active: false
        },
        { active: false }
      ],
      filterSalary: 0,
      filterTime: 9999,
      filterName: ['large', 'affiliate', 'medium', 'venture', 'small'],
      filterSize: [
        {
          id: 1,
          name: '대기업',
          size: 'large',
          active: true
        },
        {
          id: 2,
          name: '대기업 계열사·자회사',
          size: 'affiliate',
          active: true
        },
        { id: 3, name: '중견기업', size: 'medium', active: true },
        { id: 4, name: '벤처기업', size: 'venture', active: true },
        { id: 5, name: '중소기업', size: 'small', active: true }
      ],
      filterRecruiting: true
    }
  },
  computed: {
    ...mapGetters('company', ['getAllCompanies'])
  },
  methods: {
    ...mapMutations('localStorage', ['setFilterList', 'setFilteredCompanies']),
    handleFilter() {
      let filterData = {}
      filterData = {
        salary: this.filterSalary,
        time: this.filterTime >= 90 ? 9999 : this.filterTime,
        size: this.filterSize.map((v) => v.name),
        recruiting: this.filterRecruiting
      }
      this.setFilterList(filterData)
      const companyData = this.getAllCompanies
      let data = []
      if (filterData.recruiting) {
        data = companyData.filter((v) => {
          return (
            v.avg_salary !== '회사내규에 따름' &&
            v.avg_salary >= filterData.salary &&
            v.transitTime <= filterData.time &&
            filterData.size.includes(v.scale) &&
            v.jobs_count >= 1
          )
        })
      } else {
        data = companyData.filter((v) => {
          return (
            v.avg_salary !== '회사내규에 따름' &&
            v.avg_salary >= filterData.salary &&
            v.transitTime <= filterData.time &&
            filterData.size.includes(v.scale)
          )
        })
      }
      this.setFilteredCompanies(data)
      for (let i = 0; i < 4; i++) {
        this.menuController[i].active = false
      }
    },
    handleMenu(idx) {
      if (this.menuController[idx].active) {
        this.menuController[3].active = false
        this.menuController[idx].active = false
      } else {
        this.menuController[3].active = true
        for (let i = 0; i < 3; i++) {
          if (i === idx) {
            this.menuController[i].active = true
          } else {
            this.menuController[i].active = false
          }
        }
      }
    },
    handleToggle(idx) {
      this.filterSize[idx].active = !this.filterSize[idx].active
    },
    handleRecruiting() {
      this.filterRecruiting = !this.filterRecruiting
    }
  }
}
</script>

<style lang="scss" scoped>
.filter-list {
  width: 100%;
  display: flex;
  flex-direction: column;
  border-top: 1px solid #8774c1;
}
.filter-items {
  width: 100%;
  display: flex;
  box-sizing: border-box;
  justify-content: space-between;
  border-bottom: 1.5px solid #8774c1;
  background-color: #fff;
  div {
    padding-top: 10px;
    &:hover {
      background-color: #8774c1;
    }
  }
}

.filter-item {
  width: 33.333333333%;
  box-sizing: border-box;
  text-align: center;
  padding-bottom: 10px;
  cursor: pointer;
  &:last-child {
    width: 0;
  }
}

.filter-detail {
  z-index: 18;
  border-radius: 0 0 10px 10px;
  padding-bottom: 10px;
  background-color: #fff;
  border-bottom: 1.5px solid #8774c1;
  div {
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 18;
    background-color: #fff;
    p {
      min-width: 70px;
      max-width: 70px;
    }
  }
}

.filter-detail-size {
  display: flex;
  flex-direction: column;
  justify-content: flex-start !important;
  align-items: flex-start !important;
  padding: 10px;
  div + div {
    margin-top: 10px;
  }
  i,
  label {
    cursor: pointer;
  }
  i + label {
    margin-left: 5px;
  }
  input {
    margin-top: 5px;
    display: none !important;
  }
  input,
  label {
    display: inline-block;
  }
}

.filter-recruiting {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  input {
    display: none;
  }
  i,
  label {
    cursor: pointer;
  }
}

.filter-bottom {
  display: flex;
  flex-direction: column;
  button {
    margin-top: 15px;
    background-color: #8774c1;
    border-radius: 5px;
    padding: 8px 15px;
    color: #fff;
  }
}

input[type='range'] {
  -webkit-appearance: none;
  margin: 18px;
  width: 60%;
}
input[type='range']:focus {
  outline: none;
}
input[type='range']::-webkit-slider-runnable-track {
  width: 60%;
  height: 8.4px;
  cursor: pointer;
  animate: 0.2s;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  background: #8774c1;
  border-radius: 1.3px;
  border: 0.2px solid #010101;
}
input[type='range']::-webkit-slider-thumb {
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  border: 1px solid #000000;
  height: 16px;
  width: 16px;
  border-radius: 3px;
  background: #ffffff;
  cursor: pointer;
  -webkit-appearance: none;
  margin-top: -4px;
}
input[type='range']:focus::-webkit-slider-runnable-track {
  background: #8774c1;
}
input[type='range']::-moz-range-track {
  width: 60%;
  height: 8.4px;
  cursor: pointer;
  animate: 0.2s;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  background: #8774c1;
  border-radius: 1.3px;
  border: 0.2px solid #010101;
}
input[type='range']::-moz-range-thumb {
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  border: 1px solid #000000;
  height: 16px;
  width: 16px;
  border-radius: 3px;
  margin-top: -4px;
  background: #ffffff;
  cursor: pointer;
}
input[type='range']::-ms-track {
  width: 60%;
  height: 8.4px;
  padding-top: 10px;
  cursor: pointer;
  animate: 0.2s;
  background: transparent;
  border-color: transparent;
  border-width: 16px 0;
  color: transparent;
}
input[type='range']::-ms-fill-lower {
  background: #8774c1;
  border: 0.2px solid #010101;
  border-radius: 2.6px;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
}
input[type='range']::-ms-fill-upper {
  background: #8774c1;
  border: 0.2px solid #010101;
  border-radius: 2.6px;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
}
input[type='range']::-ms-thumb {
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  border: 1px solid #000000;
  height: 16px;
  width: 16px;
  border-radius: 3px;
  margin-top: -4px;
  background: #ffffff;
  cursor: pointer;
}
input[type='range']:focus::-ms-fill-lower {
  background: #8774c1;
}
input[type='range']:focus::-ms-fill-upper {
  background: #8774c1;
}
</style>
