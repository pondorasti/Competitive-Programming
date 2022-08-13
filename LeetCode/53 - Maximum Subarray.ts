function maxSubArray(nums: number[]): number {
  const dp = [nums[0]]
  let ans = dp[0]

  for (let i = 1; i < nums.length; i += 1) {
    dp[i] = Math.max(dp[i - 1] + nums[i], nums[i])

    ans = Math.max(ans, dp[i])
  }

  return ans
}
