<template>
  <GmapInfoWindow
    :options="options"
    :position="position"
    :opened="open"
  ></GmapInfoWindow>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'

export default {
  name: 'MapInfoWindow',
  computed: {
    ...mapGetters({
      open: 'infoWindow/getShowInfoWindow',
      position: 'infoWindow/getInfoWindowPosition',
      optionsContent: 'infoWindow/getInfoWindowOptionsContent'
    }),
    ...mapGetters('localStorage', ['getDepartureStationName']),
    content_time() {
      const time = this.optionsContent.time
      let className = 'default'
      if (time <= 30) {
        className = 'closest'
      } else if (time <= 45) {
        className = 'closer'
      } else if (time <= 60) {
        className = 'close'
      }
      return `<span class="${className}">
                <i class="material-icons-round">departure_board</i>
              </span>약 ${time}분 (${this.getDepartureStationName}역 기준)`
    },
    content_salary() {
      const jobs = this.optionsContent.jobs
      if (!jobs) {
        return `<div class="noJobs">
                  <i class="material-icons-round">error</i>
                  현재 진행 중인 채용 공고가 없습니다.
                </div>`
      }
      const salary = this.optionsContent.salary
      let className = ''
      if (salary === 0) {
        return `<div class="salaryInfo">
                  <i class="material-icons-round">monetization_on</i>
                  연봉: 회사 내규에 따름
                </div>`
      } else if (salary >= 5000) {
        className = 'higher'
      } else if (salary >= 4000) {
        className = 'high'
      }
      return `<div class="salaryInfo">
                <i class="material-icons-round ${className}">monetization_on</i>
                연봉 ${salary}만원
              </div>`
    },
    options() {
      return {
        content: `<div class="infWinContainer">
                    <div class="Title">${this.optionsContent.name}</div>
                    <div class="Detail">
                      <div class="Time">
                        ${this.content_time}
                      </div>
                      <div class="Salary">
                        ${this.content_salary}
                      </div>
                    </div>
                  </div>`,
        pixelOffset: {
          width: -7,
          height: -45
        }
      }
    }
  },
  methods: {
    ...mapMutations('infoWindow', ['setShowInfoWindow']),
    enableInfoWindow() {
      this.setShowInfoWindow(true)
    },
    disableInfoWindow() {
      setTimeout(() => {
        this.setShowInfoWindow(false)
      }, 400)
    }
  }
}
</script>

<style lang="scss">
//// Global CSS Styling /////

// 1) Override default info window styles
.gm-style .gm-style-iw-c {
  min-width: 160px !important;
  height: auto !important;
  background: white;
  padding: 0 !important;
  border-radius: 3px !important;
  button {
    display: none !important;
  }
  & > .gm-style-iw-d,
  & > .gm-style-iw-d > div {
    min-width: 160px !important;
    height: auto !important;
    overflow-x: hidden !important;
  }
}

// 2) Control internal content styles, i.e options.content
.infWinContainer {
  width: 100%;
  height: auto;
  background: white;
  padding: 10px;
  & > .Title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
    white-space: nowrap;
  }
  & > .Detail {
    & > .Time {
      span {
        width: 10px;
        height: 10px;
        margin-right: 8px;
        color: rgb(80, 29, 67);
        display: inline-block;
        i {
          font-size: 1.1em;
          position: relative;
          transform: translateY(2px);
        }
        &.closest {
          color: rgb(236, 99, 66);
        }
        &.closer {
          color: rgb(183, 38, 61);
        }
        &.close {
          color: rgb(132, 30, 62);
        }
      }
    }
    & > .Salary {
      & > .noJobs {
        color: gray;
        i {
          font-size: 1.1em;
          position: relative;
          transform: translateY(2px);
        }
      }
      & > .salaryInfo {
        i {
          font-size: 1.1em;
          position: relative;
          transform: translateY(2px);
          color: gray;
          &.higher {
            color: rgb(131, 191, 65);
          }
          &.high {
            color: rgb(248, 211, 71);
          }
        }
      }
    }
  }
}
</style>
