function shortestPathBinaryMatrix(grid: number[][]): number {
  const size = grid.length
  const directions = [
    { dx: 1, dy: 0 },
    { dx: -1, dy: 0 },
    { dx: 0, dy: 1 },
    { dx: 0, dy: -1 },
    { dx: 1, dy: -1 },
    { dx: -1, dy: 1 },
    { dx: 1, dy: 1 },
    { dx: -1, dy: -1 },
  ]

  function isValid(x: number, y: number): boolean {
    if (x < 0 || x >= size) return false
    if (y < 0 || y >= size) return false
    if (grid[x][y] === 0) return true
    return false
  }

  function hashPoint(x: number, y: number): string {
    return `x:${x};y:${y}`
  }

  // is starting point is not valid, exit early
  if (!isValid(0, 0)) return -1

  const visited = new Set()
  const queue: { x: number; y: number; length: number }[] = [{ x: 0, y: 0, length: 1 }]
  while (queue.length !== 0) {
    const { x, y, length } = queue.pop()!

    if (x === size - 1 && y === size - 1) return length

    directions.forEach(({ dx, dy }) => {
      const newX = x + dx
      const newY = y + dy

      if (!isValid(newX, newY)) return
      if (visited.has(hashPoint(newX, newY))) return

      visited.add(hashPoint(newX, newY))
      queue.unshift({ x: newX, y: newY, length: length + 1 })
    })
  }

  return -1
}
