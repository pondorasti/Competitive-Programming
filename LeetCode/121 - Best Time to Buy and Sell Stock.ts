function maxProfit(prices: number[]): number {
  let ans = 0
  let minValue = prices[0]

  for (let i = 1; i < prices.length; i += 1) {
    ans = Math.max(ans, prices[i] - minValue)
    minValue = Math.min(minValue, prices[i])
  }

  return ans
}
