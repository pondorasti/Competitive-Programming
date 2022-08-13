function searchMatrix(matrix: number[][], target: number): boolean {
  const numberOfRows = matrix.length
  const numberOfCols = matrix[0].length

  let left = 0
  let right = numberOfRows * numberOfCols - 1

  while (left <= right) {
    const middle = Math.floor((left + right) / 2)
    const row = Math.floor(middle / numberOfCols)
    const col = middle % numberOfCols

    if (matrix[row][col] === target) {
      return true
    } else if (matrix[row][col] < target) {
      left = middle + 1
    } else {
      right = middle - 1
    }
  }

  return false
}
