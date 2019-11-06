export const state = () => ({
  departureStationID: 961,
  departureStationName: '역삼',

  // Center & zoom level of last viewed map region
  // Stored in local storage, updated via map '@dragend', i.e after each complete drag event
  // Used to keep track of map position upon page reload
  // Initial latitude/longitude values point to Multicampus
  // 마지막으로 조회한 지도 중심 좌표 및 줌 레벨
  // 로컬스토리지에 저장되며 지도 드래그 시 업데이트됨
  // 사이트 리로드시 마지막으로 조회한 지도 영역을 그대로 보여주기 위함
  // 초기 위도/경도 값은 멀티캠퍼스 위치임
  lastCenterLat: 37.5012,
  lastCenterLng: 127.0396,
  lastZoom: 0,
  filteredCompanies: [],
  filterList: {
    time: '',
    salary: '',
    size: [
      {
        id: 1,
        name: '대기업',
        size: 'large',
        active: true
      },
      {
        id: 2,
        name: '대기업 계열사·자회사',
        size: 'affiliate',
        active: true
      },
      { id: 3, name: '중견기업', size: 'medium', active: true },
      { id: 4, name: '벤처기업', size: 'venture', active: true },
      { id: 5, name: '중소기업', size: 'small', active: true }
    ],
    recruiting: false
  }
})

export const getters = {
  getDepartureStationID: (state) => state.departureStationID,
  getDepartureStationName: (state) => state.departureStationName,
  getLastCenterLat: (state) => state.lastCenterLat,
  getLastCenterLng: (state) => state.lastCenterLng,
  getLastZoom: (state) => state.lastZoom,
  getFilterList: (state) => state.filterList,
  getFilteredCompanies: (state) => state.filteredCompanies
}

export const mutations = {
  setDepartureStationID: (state, payload) => {
    state.departureStationID = payload
  },
  setDepartureStationName: (state, payload) => {
    state.departureStationName = payload
  },
  setLastCenterLat: (state, payload) => {
    state.lastCenterLat = payload
  },
  setLastCenterLng: (state, payload) => {
    state.lastCenterLng = payload
  },
  setLastZoom: (state, payload) => {
    state.lastZoom = payload
  },
  setFilterList: (state, payload) => {
    state.filterList = payload
  },
  setFilterListSize: (state, payload) => {
    state.filterList.size[payload].active = !state.filterList.size[payload]
      .active
  },
  setFilteredCompanies: (state, payload) => {
    state.filteredCompanies = payload
  }
}
