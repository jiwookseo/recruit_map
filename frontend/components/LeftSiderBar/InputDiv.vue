<template>
  <div class="left--side-search-div">
    <div class="left--side-bar-input">
      <input
        v-model="searchText"
        type="text"
        placeholder="Input text in here"
      />
      <!--
        최근 검색 기록은 5개씩, localStorage에 저장하여 보여주는 것으로 대체한다.
        [
          {
          "type":"SEARCH_WORD",
          "name":"낙성대역",
          "updateTime":1571799901369
          },
          {
            "id":"227",
            "name":"낙성대역 2호선",
            "address":"서울특별시 관악구 남부순환로 1928",
            "type":"SUBWAY_STATION",
            "longitude":126.9634334,
            "latitude":37.4771259,
            "updateTime":1571799901347
          },
          {
            "type":"SEARCH_WORD",
            "name":"분당치과",
            "updateTime":1571799892952
          }
        ]
      -->
      <div v-if="setActivateSearch" class="left--side-bar-filterList">
        <p v-for="idx in 5" :key="idx">카카카</p>
      </div>
    </div>
    <div class="left--side-bar-filter"></div>
  </div>
</template>

<script>
export default {
  name: 'InputDiv',
  data() {
    return {
      searchText: ''
    }
  },
  computed: {
    setActivateSearch() {
      if (this.searchText.length > 2) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>
<style lang="scss">
.left--side-bar-input {
  display: flex;
  flex-direction: column;
  input[type='text'] {
    background-color: #fff;
    border: none;
    outline: none;
    width: 100%;
    min-height: 50px;
    &::placeholder {
      font-size: 24px;
    }
  }
}

.left--side-bar-filterList {
  p {
    height: 58px;
    background-color: #8774c1;
    color: #fff;
    font-size: 18px;
    font-weight: 500;
    padding: 15px 0 15px 10px;
  }
}
</style>
