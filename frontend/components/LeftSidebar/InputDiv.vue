<template>
  <div class="left--side-search-div">
    <div class="left--side-bar-input">
      <input
        v-model="searchText"
        type="text"
        placeholder="회사 명을 입력하세요"
        @input="handleChange"
      />
      <div
        v-if="searchButton"
        v-click-outside="handleSwitch"
        class="left--side-bar-filterList"
      >
        <p
          v-for="item in computedCompanyList"
          :key="item.id"
          @click="moveDetail(item)"
        >
          {{ item.name }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../../api/company'
import { mapMutations, mapGetters } from 'vuex'
export default {
  name: 'InputDiv',
  data() {
    return {
      searchText: '',
      searchedCompanies: [],
      searchButton: false
    }
  },
  computed: {
    ...mapGetters('localStorage', [
      'getLastZoom',
    ]),
    computedCompanyList() {
      if (this.searchedCompanies.length > 4) {
        return this.searchedCompanies.slice(0, 5)
      } else {
        return this.searchedCompanies
      }
    }
  },

  methods: {
    async handleChange() {
      if (this.searchText.length >= 1) {
        this.searchButton = true
      } else {
        this.searchButton = false
      }
      if (this.searchButton) {
        const res = await api.getCompanyDataByName(this.searchText)
        this.searchedCompanies = res.data.results
        this.$store.commit('leftSidebar/setShowSearchbar', true)
      } else {
        this.$store.commit('leftSidebar/setShowSearchbar', false)
      }
    },
    handleSwitch() {
      this.searchButton = false
    },
    moveDetail(data) {
      this.searchText = ''
      this.$store.commit('leftSidebar/setShowSearchbar', false)
      this.$store.commit('maps/setTargetCenterLat', data.lat)
      this.$store.commit('maps/setTargetCenterLng', data.lng)
      const zoomDiff = this.getLastZoom - 17;
      if (zoomDiff > 0) {
        let zoom = this.getLastZoom
        let i = setInterval(() => {
          zoom--
          this.$store.commit('localStorage/setLastZoom', zoom)
          if (zoom === 17) {
            clearInterval(i)
          }
        }, 100);
      }
      else if (zoomDiff < 0) {
        let zoom = this.getLastZoom
        let i = setInterval(() => {
          zoom++
          this.$store.commit('localStorage/setLastZoom', zoom)
          if (zoom === 17) {
            clearInterval(i)
          }
        }, 100);
      }
      this.$store.dispatch('company/setAsyncCompanyDetail', data.id)
      this.searchButton = false
      this.$router.push(`/company/${data.id}`)
    }
  }
}
</script>
<style lang="scss">
.left--side-bar-input {
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  outline: none;
  input[type='text'] {
    background: none #fff;
    outline: none;
    min-height: 50px;
    padding-left: 20px;
    font-weight: 600;
    border: 2px solid #fff;
    border-radius: 2px;
    &::placeholder {
      font-size: 18px;
      font-weight: 400;
    }
    &:focus {
      border-color: #755eb5;
    }
  }
}

.left--side-bar-filterList {
  background-color: #fff;
  box-sizing: border-box;
  border-radius: 0 0 10px 10px;
  border: 2px solid #8774c1;
  z-index: 10;
  padding: 0 1px;
  p {
    box-sizing: border-box;
    height: 58px;
    color: #181818;
    font-size: 14px;
    font-weight: 400;
    padding: 15px 0 15px 10px;
    cursor: pointer;
    &:hover {
      background-color: #eee;
    }
    &:last-child {
      border-radius: 0 0 10px 10px;
    }
    a {
      text-decoration: none;
      color: #181818;
    }
  }
}
</style>
