function matrixReshape(mat: number[][], r: number, c: number): number[][] {
  const m = mat.length
  const n = mat[0].length

  if (m * n !== r * c) return mat

  let originalRow = 0
  let originalColumn = 0
  let reshapeRow = 0
  let reshapeColumn = 0

  let ansMat = [[]]
  while (reshapeRow < r) {
    while (originalColumn < mat[originalRow].length) {
      ansMat[reshapeRow][reshapeColumn] = mat[originalRow][originalColumn]
      originalColumn += 1

      reshapeColumn += 1
      if (reshapeColumn >= c) {
        reshapeColumn = 0
        reshapeRow += 1
        if (reshapeRow < r) ansMat.push([])
      }
    }

    originalColumn = 0
    originalRow += 1
  }

  return ansMat
}
