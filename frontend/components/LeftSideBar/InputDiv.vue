<template>
  <div class="left--side-search-div">
    <div class="left--side-bar-input">
      <input
        v-model="searchText"
        type="text"
        placeholder="회사 명 또는 지하철 역을 입력하세요"
        @input="handleChange"
      />
      <div v-if="setActivateSearch" class="left--side-bar-filterList">
        <p
          v-for="item in computedMovieList"
          @click="moveDetail(item.id)"
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
      searchedMovie: []
    }
  },
  computed: {
    setActivateSearch() {
      return this.searchText.length >= 1
    },
    computedMovieList() {
      if (this.searchedMovie.length > 4) {
        return this.searchedMovie.slice(0, 5)
      } else {
        return this.searchedMovie
      }
    }
  },
  // search 구현하기
  methods: {
    async handleChange() {
      if (this.setActivateSearch) {
        let res = await api.getCompanyDataByName(this.searchText)
        this.searchedMovie = res.data.results
        this.$store.commit('leftSideBar/setSearchShow', true)
      } else {
        this.$store.commit('leftSideBar/setSearchShow', false)
      }
    },
    moveDetail(id) {
      this.searchText = ''
      if (this.$refs.filterList) {
        // this.$refs.sideSearch.style.zIndex = 8
        // this.$refs.lsb.style.zIndex = '7 important!'
      }
      this.$router.push(`/company/${id}`)
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
    width: 100%;
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
