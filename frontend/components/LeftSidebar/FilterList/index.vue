<template>
  <div class="filter-list">
    <div class="filter-items" :class="{'thickBorder': !menuController[3].active}">
      <div
        v-for="(menuItem, i) in menuController"
        :key="menuItem.id"
        class="filter-item"
        :class="{'active': menuController[i].active}"
        @click="handleMenu(i)"
      >
        <span>{{ menuItem.name }}</span>
      </div>
    </div>
    <div v-show="menuController[3].active" class="filter-detail">
      <div class="filter-top">
        <!-- 연봉 -->
        <div v-show="menuController[0].active" class="filter-detail-salary">
          <input v-model="filterSalary" type="range" min="0" max="6000" value="0" step="100" />
          <span>{{ filterSalary }} 만원</span>
        </div>
        <!-- 시간 -->
        <div v-show="menuController[1].active" class="filter-detail-time">
          <input v-model="filterTime" type="range" min="15" max="90" value="15" step="15" />
          <span>{{ filterTime >= 90 ? '90분 이상' : filterTime + '분 이내' }}</span>
        </div>
        <!-- 규모 -->
        <client-only>
          <div v-show="menuController[2].active" class="filter-detail-size">
            <!-- { major: '대기업', affiliate:'대기업 계열사·자회사', venture: '벤처기업', midSize: '중견기업', smallSize:'중소기업'}  -->
            <div
              v-for="(item, idx) in filterSize"
              :key="item.id"
              class="filter-detail-size-item"
              v-show="menuController[2].active"
            >
              <input
                :id="item.size"
                v-model="filterSize[idx]"
                type="checkbox"
                :value="item.size"
                :checked="item.active"
              />
              <i
                class="material-icons-round"
                v-if="filterSize[idx].active"
                @click="handleToggle(idx)"
              >check_box</i>
              <i
                class="material-icons-round"
                v-else
                @click="handleToggle(idx)"
              >check_box_outline_blank</i>
              <span @click="handleToggle(idx)">{{ item.name }}</span>
            </div>
          </div>
        </client-only>
      </div>
      <!-- 현재 채용 중인 공고만 보기 + 적용하기 버튼 -->
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
        <div class="btnBox">
          <button class="applyFilterBtn" @click="handleFilter">적용하기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
import { filterCompanySize } from '../../../lib/filter'
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
      filterRecruiting: true
    }
  },
  computed: {
    ...mapGetters('company', ['getAllCompanies']),
    ...mapGetters('localStorage', ['getFilterList']),
    filterSize: {
      get() {
        return this.getFilterList.size
      },
      set(idx) {
        this.setFilterList.size[idx].active = !this.getFilterList.size[idx]
          .active
      }
    }
  },
  methods: {
    ...mapMutations('localStorage', [
      'setFilterList',
      'setFilteredCompanies',
      'setFilterListSize'
    ]),
    ...mapMutations('leftSidebar', ['setNoDataAlert']),
    handleFilter() {
      let scaleData = filterCompanySize(this.filterSize)
      let filterData = {}
      filterData = {
        salary: this.filterSalary,
        time: this.filterTime >= 90 ? 9999 : this.filterTime,
        size: this.filterSize,
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
            scaleData.includes(v.scale) &&
            v.jobs_count >= 1
          )
        })
      } else {
        data = companyData.filter((v) => {
          return (
            v.avg_salary !== '회사내규에 따름' &&
            v.avg_salary >= filterData.salary &&
            v.transitTime <= filterData.time &&
            scaleData.includes(v.scale)
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
      this.setFilterListSize(idx)
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
  height: auto;
  border-top: 2px solid #8774c1;
  position: absolute;
  top: 60px;
}
.filter-items {
  width: 100%;
  display: flex;
  box-sizing: border-box;
  justify-content: space-between;
  border: 1.5px solid #8774c1;
  border-top: none;
  border-bottom-width: 1px;
  background-color: #fff;
  &.thickBorder {
    border-bottom-width: 2px;
  }
  div {
    padding-top: 10px;
    // &:hover {
    //   border-bottom-color: #dbd0ff;
    //   background-color: #dbd0ff;
    // }
  }
}

.filter-item {
  width: 33.333333333%;
  box-sizing: border-box;
  text-align: center;
  padding-bottom: 10px;
  cursor: pointer;
  border-bottom: 3px solid white;
  &:last-child {
    width: 0;
  }
  &.active {
    border-bottom-color: #7564a7;
  }
}

.filter-detail {
  z-index: 18;
  border-radius: 0 0 5px 5px;
  background-color: #f8f8f8;
  border: 1.5px solid #8774c1;
  border-top: none;
  height: 180px;
  .filter-top {
    height: 110px;
    position: relative;
  }
  .filter-bottom {
    height: calc(100% - 110px);
    position: relative;
    input {
      display: none;
    }
  }
}

.filter-detail-salary,
.filter-detail-time {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  height: 50px;
  padding-left: 45px;
  & > span {
    position: absolute;
    top: 3px;
    right: 45px;
  }
}

.filter-detail-size {
  padding: 20px 0 0 20px;
  input {
    display: none;
  }
  .filter-detail-size-item {
    float: left;
    margin-right: 15px;
    &:nth-child(2) {
      margin-left: 15px;
    }
    &:nth-child(3) {
      clear: both;
    }
    i {
      color: rebeccapurple;
      user-select: none;
      cursor: pointer;
    }
    span {
      position: relative;
      top: -5px;
    }
  }
}

.filter-recruiting {
  padding-left: 80px;
  i {
    user-select: none;
    cursor: pointer;
    color: #181818;
  }
  label {
    position: relative;
    top: -5px;
  }
}

.btnBox {
  position: relative;
  margin-top: 5px;
  .applyFilterBtn {
    padding: 3px 10px;
    border-radius: 3px;
    background: rebeccapurple;
    color: white;
    font-size: 13px;
    margin: 0 auto;
    position: absolute;
    left: 50%;
    transform: translate(-50%);
    font-weight: 400;
    transition: all 0.2s;
    &:focus {
      outline: none;
    }
    &:hover {
      background: rgb(81, 40, 122);
    }
  }
}

// div {
//   display: flex;
//   justify-content: center;
//   align-items: center;
//   z-index: 18;
//   background-color: #fff;
//   &:first-child,
//   &:nth-child(2) {
//     align-items: flex-end;
//   }
//   p {
//     min-width: 70px;
//     max-width: 70px;
//   }
// }

// .filter-detail-size {
//   display: block !important;
//   padding: 10px;
//   i,
//   label {
//     cursor: pointer;
//   }
//   i + label {
//     margin-left: 5px;
//   }
//   input {
//     margin-top: 5px;
//     display: none !important;
//   }
//   input,
//   label {
//     display: inline-block;
//   }
// }

// .filter-recruiting {
//   display: flex;
//   align-items: center;
//   justify-content: flex-start;
//   input {
//     display: none;
//   }
//   i,
//   label {
//     cursor: pointer;
//   }
// }

// .filter-bottom {
//   clear: both;
//   display: flex;
//   flex-direction: column;
//   padding-top: 21.7px;
//   button {
//     margin-top: 15px;
//     background-color: #8774c1;
//     border-radius: 5px;
//     padding: 8px 15px;
//     color: #fff;
//   }
// }

// .filter-detail-size-item {
//   float: left;
//   &:nth-child(2) {
//     margin-left: 17px;
//     margin-bottom: 6.4px;
//   }
//   &:nth-child(3) {
//     clear: both;
//   }
//   &:nth-child(4) {
//     margin-left: 2px;
//   }
//   &:last-child {
//     margin-left: 15px;
//   }
// }

input[type='range'] {
  -webkit-appearance: none;
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
