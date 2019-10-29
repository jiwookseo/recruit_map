<template>
  <div class="outer">
    <div class="currentStation">
      출발: {{ currentStation.name || getDepartureStationName }}역
      <button class="btn" @click="applyChanges" :disabled="!valid">적용</button>
    </div>
    <div class="changeStation">
      <input v-model="searchString" placeholder="지하철역을 검색하세요">
      <ul class="scrollable">
        <li v-for="st in filteredStations" :key="st.id" @click="setStation(st)">
          {{st.name}}
          <div class="line" v-for="line in st.line.split(',')" :key="line.id" :class="`L${line}`">
            {{lineName(line)}}
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapMutations, mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: "StationMenu",
  data: () => ({
    searchString: '',
    currentStation: {
      name: "",
      id: 0
    }
  }),
  computed: {
    ...mapGetters('company', [
      'getAllCompanies',
    ]),
    ...mapGetters('station', [
      'getDepartureStationID',
      'getDepartureStationName',
      'getRoutesFromStation',
      'getAllStations'
    ]),
    filteredStations() {
      let searchString = this.searchString;
      return this.getAllStations.filter(st => {
        return st.name.includes(searchString)
      })
    },
    valid() {
      if (!this.currentStation.name) {
        return false
      }
      if (this.currentStation.name === this.getDepartureStationName) {
        return false
      }
      else {
        return true
      }
    },
  },
  methods: {
    ...mapMutations('company', [
      'setAllCompanies',
    ]),
    ...mapMutations('station', [
      'setDepartureStationID',
      'setDepartureStationName',
      'setRoutesFromStation',
      'setShowStationMenu',
      'setShowStationAlert'
    ]),
    lineName(line) {
      if (line === 'A') {
        return '공항'
      }
      else if (line === 'B') {
        return '분당'
      }
      else if (line === 'E') {
        return '에버라인'
      }
      else if (line === 'G') {
        return '경춘'
      }
      else if (line === 'I') {
        return '인천 1'
      }
      else if (line === 'I2') {
        return '인천 2'
      }
      else if (line === 'K') {
        return '경의중앙'
      }
      else if (line === 'SU') {
        return '수인'
      }
      else if (line === 'U') {
        return '의정부'
      }
      else {
        return line
      }
    },
    setStation(st) {
      this.currentStation.name = st.name;
      this.currentStation.id = st.id;
    },
    applyChanges() {
      // Change departure station in Vuex
      this.setDepartureStationName(this.currentStation.name);
      this.setDepartureStationID(this.currentStation.id);
      
      const APIBase = 'http://52.78.29.170:8000/api/';
      axios
        // Get all possible routes from newly set departure station
        .get(`${APIBase}stations/${this.currentStation.id}/routes`)
        .then((res) => {
          this.setRoutesFromStation(res.data)
        })
        // Update transit time for each company
        .then(() => {
          axios.get(`${APIBase}companies/?all`).then((res) => {
            let companies = res.data;
            const routes = this.getRoutesFromStation;
            companies.forEach((c) => {
              const route = routes.find(function(r) {
                return r.company === c.id
              });
              if (route) {
                c.transitTime = route.time;
              }
            })
            this.setAllCompanies(companies);
          })
        });
      this.searchString = '';
      this.setShowStationMenu(false);
      this.setShowStationAlert(true);
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
    top: -2px;
    &:focus {
      outline: none;
    }
    &:hover {
      background: #663399;
    }
    &:disabled {
      background: #CCC;
    }
  }
}
.changeStation {
  & > input {
    width: 100%;
    height: 30px;
    border-radius: 2px;
    border: 1px solid gray;
    font-size: 0.9em;
    margin-bottom: 5px;
    padding: 0 5px;
    &:focus {
      outline: none;
    }
  }
  & > ul {
    max-height: 150px;
    border-radius: 2px;
    border: 1px solid gray;
    list-style: none;
    overflow-y: auto;
    font-size: 0.9em;
    & > li {
      padding: 2px 5px;
      user-select: none;
      cursor: pointer;
      &:hover {
        background: #EEE;
      }
      & > .line {
        display: inline-block;
        min-width: 16px;
        height: 16px;
        line-height: 16px;
        border-radius: 16px;
        padding: 1px 5px 0;
        background: #3CB44A;
        color: white;
        font-size: 10px;
        font-weight: bold;
        text-align: center;
        margin-left: 2px;
        &.L1 {
          background: #263C96;
        }
        &.L3 {
          background: #F06E00;
        }
        &.L4 {
          background: #2C9EDE;
        }
        &.L5 {
          background: #8936E0;
        }
        &.L6 {
          background: #B5500B;
        }
        &.L7 {
          background: #697215;
        }
        &.L8 {
          background: #E51E6E;
        }
        &.L9 {
          background: #D1A62C;
        }
        &.LA {
          background: #73B6E4;
        }
        &.LB {
          background: #EBA900;
        }
        &.LE {
          background: #77C371;
        }
        &.LG {
          background: #08AF7B;
        }
        &.LI {
          background: #6F99D0;
        }
        &.LI2 {
          background: #F4AB3E;
        }
        &.LK {
          background: #7CC4A5;
        }
        &.LSU {
          background: #EBA900;
        }
        &.LU {
          background: #FF9D27;
        }
      }
    }
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