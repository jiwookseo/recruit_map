export function filterCompanySize(filterSizeArr) {
  let scaleData = []
  for (let i = 0; i < 5; i++) {
    if (filterSizeArr[i].active) {
      scaleData.push(filterSizeArr[i].name)
    }
  }
  return scaleData
}
