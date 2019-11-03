<template>
  <div class="filter-list">
    <div class="filter-items">
      <div class="filter-item-salary">
        연봉
      </div>
      <div class="filter-item-time">
        시간
      </div>
      <div class="filter-item-time">
        규모
      </div>
    </div>
    <div>
      <input type="range" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'FilterList'
}
</script>

<style lang="scss" scoped>
.filter-list {
  width: 95%;
  height: 80px;
  display: flex;
  flex-direction: row;
  background-color: white;
  padding-top: 10px;
}
.filter-items {
  width: 100%;
  display: flex;
  justify-content: space-around;
}
</style>