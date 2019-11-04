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
    <div class="filter-detail">
      <div v-show="menuController[0].active" class="filter-detail-salary">
        <input
          v-model="filterSalary"
          type="range"
          min="0"
          max="6000"
          value="0"
          step="100"
        />
        <p>{{ filterSalary }}</p>
      </div>
      <div v-show="menuController[1].active" class="filter-detail-time">
        <input
          v-model="filterTime"
          type="range"
          min="15"
          max="90"
          value="15"
          step="15"
        />
        <p>{{ filterTime >= 90 ? '90분 이상' : filterTime }}</p>
      </div>
      <div v-show="menuController[2].active" class="filter-detail-size">
        <!-- { major: '대기업', affiliate:'대기업 계열사·자회사', venture: '벤처기업', midSize: '중견기업', smallSize:'중소기업'}  -->
        <div
          v-for="(item, idx) in filterSize"
          :key="item.id"
          class="filter-detail-size-item"
        >
          <input
            :id="item.size"
            v-model="filterSize[idx].active"
            type="checkbox"
            :value="item.size"
            :checked="item.active"
          />
          <label :for="item.size">{{ item.name }}</label>
        </div>
      </div>
      <div v-show="menuController[3].active">
        <input
        id="recruiting"
        v-model="filterRecruiting"
        type="checkbox"
        value="recruiting"
        :checked="filterRecruiting"
      />
        <label for="recruiting">현재 채용중인 공고만 보기</label>
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
        {active: false}
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
      const data = companyData.filter((v) => {
        return (
          v.start_salary >= filterData.salary &&
          v.transitTime <= filterData.time &&
          filterData.size.includes(v.scale) &&
          v.jobs_count >= 1
        )
      })
      console.log('data', data)
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
    }
  }
}
</script>

<style lang="scss" scoped>
.filter-list {
  width: 95%;
  display: flex;
  flex-direction: column;
  background-color: white;
  padding-top: 10px;
}
.filter-items {
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.filter-item {
  width: 33%;
  text-align: center;
  padding-bottom: 10px;
  cursor: pointer;
  &:last-child {
    width: 0;
  }
}

.filter-detail {
  div {
    z-index: 10;
    position: float;
  }
}

.filter-detail-size {
  display: flex;
  height: 200px;
  flex-direction: column;
  input,
  label {
    display: inline-block;
  }
}

.filter-detail-salary {
  height: 150px;
}
</style>
