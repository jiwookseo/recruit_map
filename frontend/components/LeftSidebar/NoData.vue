<template>
  <div class="modal-div">
    <div class="no-data-div">
      <p>해당 필터에 속해 있는 회사 채용 정보가 없습니다.</p>
      <div>
        <button @click="setNoDataAlert(false)">확인</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
export default {
  methods: {
    ...mapMutations('leftSidebar', ['setNoDataAlert'])
  }
}
</script>

<style lang="scss" scoped>
.modal-div {
  margin: -10px 0 0 -10px;
  position: absolute;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.6);
}
.no-data-div {
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  top: 33vh;
  left: 37vw;
  width: 24vw;
  height: 17vh;
  background-color: #eee;
  p {
    color: #181818;
  }
  div > button {
    padding: 5px 10px;
    background-color: #755eb5;
    color: #fff;
    font-weight: 400;
    border-radius: 10px;
    border: none;
    outline: none;
  }
}
</style>
