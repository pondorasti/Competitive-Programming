function solution(input: string): number {
  const banks = input.split("\n")

  let totalOutputJoltage = 0
  for (const bank of banks) {
    let maxJolts = 0
    const batteries = bank.split("").map(Number)

    for (let start = 0; start < batteries.length; start += 1) {
      for (let end = start + 1; end < batteries.length; end += 1) {
        const jolts = batteries[start] * 10 + batteries[end]
        maxJolts = Math.max(maxJolts, jolts)
      }
    }

    totalOutputJoltage += maxJolts
  }

  return totalOutputJoltage
}

export { solution }
