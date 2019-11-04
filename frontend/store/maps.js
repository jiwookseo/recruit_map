export const state = () => ({
  // Map center used to update the list of nearby companies (in left sidebar) in realtime
  // Updated instantaneously via map '@center_changed', i.e whenever center is changed throughout drag/zoom events
  // Initial values (upon page reload) are set to last viewed lat/lng values in local storage
  // 지도가 움직이는 동안 좌측 사이드바의 주변 기업 목록을 실시간으로 업데이트할 때 사용됨
  // 현재 조회하고 있는 지도 영역의 중심 좌표가 변경되는 즉시 바로 업데이트됨
  // 초기값은 로컬스토리지에 저장된 '마지막 조회 중심 좌표값'으로 설정됨
  realtimeCenterLat: 37.5012,
  realtimeCenterLng: 127.0396,

  // Designated map center (position designated in google map instance)
  // Used to relocate map to specified region (e.g after user selects a particular company)
  // Initial values are set to null so that the map center can reference local storage 'lastCenterLat/Lng' values upon page reload -- see <GmapMap> in default.vue
  // 지정하고자 하는 지도 중심 좌표 (구글맵 객체의 중심 좌표값으로 지정돼 있음)
  // 특정 지도 영역으로 이동하고자 할 때 이 값을 변경하면 됨 (예: 사용자가 특정 기업을 클릭하여 상세 정보를 조회하고자 할 때)
  // 초기값이 0으로 설정돼 있는 이유: 사이트 리로드한 직후에는 로컬스토리지에 저장된 '마지막 조회 중심 좌표값'을 반영하기 위함 (default.vue 의 구글맵 객체 부분 참고 바람)
  targetCenterLat: 0,
  targetCenterLng: 0
})

export const getters = {
  getRealtimeCenterLat: (state) => state.realtimeCenterLat,
  getRealtimeCenterLng: (state) => state.realtimeCenterLng,
  getTargetCenterLat: (state) => state.targetCenterLat,
  getTargetCenterLng: (state) => state.targetCenterLng,
  getLatLng: (state) => {
    return [
      {
        lat: parseFloat(parseFloat(state.realtimeCenterLat - 0.005).toFixed(7)),
        lng: parseFloat(parseFloat(state.realtimeCenterLng - 0.0035).toFixed(7))
      },
      {
        lat: parseFloat(parseFloat(state.realtimeCenterLat + 0.005).toFixed(7)),
        lng: parseFloat(parseFloat(state.realtimeCenterLng + 0.0035).toFixed(7))
      }
    ]
  }
}

export const mutations = {
  setRealtimeCenterLat: (state, payload) => {
    state.realtimeCenterLat = payload
  },
  setRealtimeCenterLng: (state, payload) => {
    state.realtimeCenterLng = payload
  },
  setTargetCenterLat: (state, payload) => {
    state.targetCenterLat = parseFloat(payload)
  },
  setTargetCenterLng: (state, payload) => {
    state.targetCenterLng = parseFloat(payload)
  }
}
