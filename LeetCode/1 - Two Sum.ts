function twoSum(nums: number[], target: number): number[] {
  const freq = new Object()

  nums.forEach((value, index) => (freq[value] = index))

  for (let index = 0; index < nums.length; index += 1) {
    const remainder = target - nums[index]
    const remainderIndex = freq[remainder]
    if (remainderIndex !== undefined && remainderIndex !== index) {
      return [index, remainderIndex]
    }
  }
}
