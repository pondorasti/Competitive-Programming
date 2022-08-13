function findBall(grid: number[][]): number[] {
  const numberOfRows = grid.length
  const numberOfCols = grid[0].length

  function findSolution(start: number): number {
    let row = 0
    let col = start

    while (row < numberOfRows) {
      if (grid[row][col] === 1 && grid[row][col + 1] === 1 && col + 1 < numberOfCols) {
        col += 1
        row += 1
      } else if (grid[row][col] === -1 && grid[row][col - 1] === -1 && col - 1 >= 0) {
        col -= 1
        row += 1
      } else {
        return -1
      }
    }

    return col
  }

  const answer = []
  for (let index = 0; index < numberOfCols; index += 1) {
    answer[index] = findSolution(index)
  }

  return answer
}
