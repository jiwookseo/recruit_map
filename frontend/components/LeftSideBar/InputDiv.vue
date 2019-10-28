<template>
  <div class="left--side-search-div">
    <div class="left--side-bar-input">
      <input
        v-model="searchText"
        type="text"
        placeholder="회사 명 또는 지하철 역을 입력하세요"
        @change="handleChange()"
      />
      <div v-if="setActivateSearch" class="left--side-bar-filterList">
        <p v-for="idx in searchedMovie" :key="idx.id+'kaka'">{{idx.name}}</p>
      </div>
    </div>
    <div class="left--side-bar-filter"></div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'InputDiv',
  data() {
    return {
      searchText: '',
      searchedMovie: []
    }
  },
  methods: {
    handleChange() {
      console.log('Change')
    }
  },
  computed: {
    setActivateSearch() {
      return this.searchText.length > 2 ? true : false
    },
    ...mapGetters('company', ['getAllCompanyCompanies'])
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
  }
}
</style>
