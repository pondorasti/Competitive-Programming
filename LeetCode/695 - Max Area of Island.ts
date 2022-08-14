function maxAreaOfIsland(grid: number[][]): number {
  const numberOfRows = grid.length
  const numberOfCols = grid[0].length
  const visited = new Set()
  let maxArea = 0

  const directions = [
    { dx: 1, dy: 0 },
    { dx: -1, dy: 0 },
    { dx: 0, dy: 1 },
    { dx: 0, dy: -1 },
  ]

  function isPointValid(x: number, y: number): boolean {
    if (x < 0 || x >= numberOfRows) return false
    if (y < 0 || y >= numberOfCols) return false

    if (grid[x][y] === 1) return true
    return false
  }

  function areaOfIsland(x: number, y: number): number {
    if (visited.has(`x:${x};y:${y}`)) return 0
    visited.add(`x:${x};y:${y}`)

    if (!isPointValid(x, y)) return 0

    let area = 1
    directions.forEach(({ dx, dy }) => {
      area += areaOfIsland(x + dx, y + dy)
    })

    return area
  }

  for (let i = 0; i < numberOfRows; i += 1) {
    for (let j = 0; j < numberOfCols; j += 1) {
      maxArea = Math.max(areaOfIsland(i, j), maxArea)
    }
  }

  return maxArea
}
