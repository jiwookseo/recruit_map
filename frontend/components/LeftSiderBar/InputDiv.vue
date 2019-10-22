<template>
  <div class="left--side-bar-input">
    <input type="text" placeholder="Input text in here" />
  </div>
</template>
<script>
export default {
  name: 'InputDiv'
}
</script>
<style lang="scss">
.left--side-bar-input {
  display: flex;
  flex-direction: column;
  height: 50px;
  input[type='text'] {
    background-color: #fff;
    border: none;
    outline: none;
    width: 100%;
    height: 100%;
    &::placeholder {
      font-size: 24px;
    }
  }
}
</style>
