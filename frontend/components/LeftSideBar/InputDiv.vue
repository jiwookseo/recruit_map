<template>
  <div class="left--side-search-div">
    <div class="left--side-bar-input">
      <input v-model="searchText" type="text" placeholder="회사 명을 입력하세요" @input="handleChange" />
      <div v-if="searchButton" class="left--side-bar-filterList" v-click-outside="handleSwitch">
        <p
          v-for="item in computedCompanyList"
          @click="moveDetail(item)"
          :key="item.id"
        >{{ item.name }}</p>
      </div>
    </div>
    <div class="left--side-bar-filter"></div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import api from '../../api/company'
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
        let res = await api.getCompanyDataByName(this.searchText)
        this.searchedCompanies = res.data.results
        this.$store.commit('leftSideBar/setSearchShow', true)
      } else {
        this.$store.commit('leftSideBar/setSearchShow', false)
      }
    },
    handleSwitch() {
      this.searchButton = false
    },
    moveDetail(data) {
      console.log(data)
      this.searchText = ''
      this.$store.commit('leftSideBar/setSearchShow', false)
      this.$store.commit('maps/setDetailLat', data.lat)
      this.$store.commit('maps/setDetailLng', data.lng)
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
    background-color: #fff;
    border: none;
    outline: none;
    width: 95%;
    min-height: 50px;
    padding-left: 20px;
    font-weight: 600;
    &::placeholder {
      font-size: 18px;
      font-weight: 400;
    }
    &:focus {
      border: 2px solid #755eb5;
    }
  }
}

.left--side-bar-filterList {
  background-color: #fff;
  width: 95.5%;
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
