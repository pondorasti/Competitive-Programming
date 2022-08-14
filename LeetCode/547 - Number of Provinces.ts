function findCircleNum(isConnected: number[][]): number {
  let numberOfProvinces = 0
  const visitedCity = new Set()

  function dfs(city: number) {
    visitedCity.add(city)

    isConnected[city].forEach((edge, index) => {
      if (edge === 1 && !visitedCity.has(index)) {
        dfs(index)
      }
    })
  }

  for (let city = 0; city < isConnected.length; city += 1) {
    if (!visitedCity.has(city)) {
      numberOfProvinces += 1
      dfs(city)
    }
  }

  return numberOfProvinces
}
