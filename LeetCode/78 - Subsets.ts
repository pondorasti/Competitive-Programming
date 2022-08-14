function subsets(nums: number[]): number[][] {
  const ans: number[][] = []
  function recursion(pos: number, set: number[]) {
    for (let index = pos + 1; index < nums.length; index += 1) {
      recursion(index, [...set, nums[index]])
    }

    ans.push(set)
  }

  recursion(-1, [])

  return ans
}
