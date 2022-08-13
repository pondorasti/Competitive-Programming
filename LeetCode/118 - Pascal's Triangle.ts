function generate(numRows: number): number[][] {
  const ans = [[1]]

  for (let row = 1; row < numRows; row += 1) {
    ans.push([])
    for (let col = 0; col < row + 1; col += 1) {
      if (col === 0 || col === row) {
        ans[row].push(1)
      } else {
        ans[row].push(ans[row - 1][col - 1] + ans[row - 1][col])
      }
    }
  }

  return ans
}
