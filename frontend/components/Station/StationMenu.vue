<template>
  <div v-click-outside="closeMenu" class="outer">
    <div class="currentStation">
      [출발] {{ currentStation.name || getDepartureStationName }}역
      <button
        class="btn"
        @click="applyChanges"
        :disabled="!valid"
      >적용</button>
    </div>
    <div class="changeStation">
      <input v-model="searchString" placeholder="지하철역을 검색하세요" autofocus />
      <i class="material-icons-round">search</i>
      <ul class="scrollable" v-if="filteredStations.length">
        <li v-for="st in filteredStations" :key="st.id" :class="{'current': st.id === currentStation.id}" @click="setStation(st)">
          {{st.name}}
          <div
            v-for="line in st.line.split(',')"
            :key="line.id"
            class="line"
            :class="`L${line}`"
          >
            {{ lineName(line) }}
          </div>
        </li>
      </ul>
      <div class="noSearchResults" v-else>검색 결과가 없습니다.</div>
    </div>
  </div>
</template>

<script>
import { mapMutations, mapGetters, mapActions } from 'vuex'

export default {
  name: 'StationMenu',
  data: () => ({
    searchString: '',
    currentStation: {
      name: '',
      id: 0
    }
  }),
  computed: {
    ...mapGetters('company', ['getAllCompanies']),
    ...mapGetters('localStorage', [
      'getDepartureStationID',
      'getDepartureStationName'
    ]),
    ...mapGetters('station', ['getRoutesFromStation', 'getAllStations']),
    filteredStations() {
      const searchString = this.searchString
      return this.getAllStations.filter((st) => {
        return st.name.includes(searchString)
      })
    },
    valid() {
      if (!this.currentStation.name) {
        return false
      }
      if (this.currentStation.name === this.getDepartureStationName) {
        return false
      } else {
        return true
      }
    }
  },
  created() {
    this.currentStation.id = this.getDepartureStationID;
  },
  methods: {
    ...mapActions('station', ['setAsyncRoutesFromStation']),
    ...mapActions('company', ['setAsyncAllCompanies']),
    ...mapMutations('company', ['setAllCompanies']),
    ...mapMutations('localStorage', [
      'setDepartureStationID',
      'setDepartureStationName'
    ]),
    ...mapMutations('station', [
      'setRoutesFromStation',
      'setShowStationMenu',
      'setShowStationAlert'
    ]),
    lineName(line) {
      if (line === 'A') {
        return '공항'
      } else if (line === 'B') {
        return '분당'
      } else if (line === 'E') {
        return '에버라인'
      } else if (line === 'G') {
        return '경춘'
      } else if (line === 'I') {
        return '인천 1'
      } else if (line === 'I2') {
        return '인천 2'
      } else if (line === 'K') {
        return '경의중앙'
      } else if (line === 'SU') {
        return '수인'
      } else if (line === 'U') {
        return '의정부'
      } else {
        return line
      }
    },
    setStation(st) {
      this.currentStation.name = st.name
      this.currentStation.id = st.id
    },
    applyChanges() {
      // Change departure station in Vuex
      this.setDepartureStationName(this.currentStation.name)
      this.setDepartureStationID(this.currentStation.id)
      this.setAsyncRoutesFromStation({
        v: this.currentStation.id,
        cb: this.setAsyncAllCompanies
      })

      // Update transit time for each company
      this.searchString = ''
      this.setShowStationMenu(false)
      this.setShowStationAlert(true)
    },
    closeMenu() {
      this.setShowStationMenu(false)
    }
  }
}
</script>

<style lang="scss" scoped>
.outer {
  width: 220px;
  height: auto;
  max-height: 250px;
  margin: 10px;
  position: absolute;
  top: 0;
  right: 50px;
  border-radius: 2px;
  box-shadow: rgba(0, 0, 0, 0.3) 0px 1px 4px -1px;
  overflow: hidden;
  background: none rgb(255, 255, 255);
  padding: 10px;
}
.currentStation {
  font-size: 0.9em;
  color: #181818;
  margin-bottom: 10px;
  position: relative;
  & > .btn {
    width: 35px;
    height: 22px;
    border-radius: 2px;
    background: #793eb4;
    color: white;
    font-size: 0.8em;
    font-weight: bold;
    position: absolute;
    right: 0;
    top: 0px;
    &:focus {
      outline: none;
    }
    &:hover {
      background: #663399;
    }
    &:disabled {
      background: #ccc;
    }
  }
}
.changeStation {
  position: relative;
  & > input {
    width: 100%;
    height: 30px;
    border-radius: 2px 2px 0 0;
    border: 1px solid #CCC;
    font-size: 0.9em;
    padding: 1px 5px 1px 25px;
    &:focus {
      outline: none;
    }
    & + i {
      color: #AAA;
      position: absolute;
      top: 6px;
      left: 5px;
      font-size: 1.2em;
      font-weight: bold;
    }
  }
  & > ul {
    max-height: 157px;
    border-radius: 0 0 2px 2px;
    border: 1px solid #CCC;
    border-top: none;
    list-style: none;
    overflow-y: auto;
    font-size: 0.9em;
    & > li {
      padding: 2px 5px;
      user-select: none;
      cursor: pointer;
      &:hover {
        background: #eee;
      }
      &.current {
        background: #eee;
      }
      & > .line {
        display: inline-block;
        min-width: 16px;
        height: 16px;
        line-height: 16px;
        border-radius: 16px;
        padding: 0 5px;
        background: #3cb44a;
        color: white;
        font-size: 10px;
        font-weight: bold;
        text-align: center;
        margin-left: 2px;
        font-family: 'Nanum Gothic Coding', monospace;
        position: relative;
        top: -2px;
        &.L1 {
          background: #263c96;
        }
        &.L3 {
          background: #f06e00;
        }
        &.L4 {
          background: #2c9ede;
        }
        &.L5 {
          background: #8936e0;
        }
        &.L6 {
          background: #b5500b;
        }
        &.L7 {
          background: #697215;
        }
        &.L8 {
          background: #e51e6e;
        }
        &.L9 {
          background: #d1a62c;
        }
        &.LA {
          background: #73b6e4;
        }
        &.LB {
          background: #eba900;
        }
        &.LE {
          background: #77c371;
        }
        &.LG {
          background: #08af7b;
        }
        &.LI {
          background: #6f99d0;
        }
        &.LI2 {
          background: #f4ab3e;
        }
        &.LK {
          background: #7cc4a5;
        }
        &.LSU {
          background: #eba900;
        }
        &.LU {
          background: #ff9d27;
        }
      }
    }
  }
  & > .noSearchResults {
    font-size: 0.8em;
    margin-top: 10px;
    color: #AAA;
  }
}

// Scrollbar
.scrollable::-webkit-scrollbar {
  display: initial;
  width: 7px;
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
  border-radius: 50px;
  -webkit-border-radius: 50px;
  &:hover {
    background-color: rgba(0, 0, 0, 0.1);
  }
}
.scrollable::-webkit-scrollbar-thumb:vertical {
  border-radius: 50px;
  -webkit-border-radius: 50px;
  background-color: rgba(0, 0, 0, 0.4);
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0);
  min-height: 10px;
  &:active {
    background-color: rgba(0, 0, 0, 0.6);
    border-radius: 50px;
    -webkit-border-radius: 50px;
  }
}
</style>
