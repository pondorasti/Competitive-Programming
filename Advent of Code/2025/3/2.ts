const MAX_DIGITS = 12

function solution(input: string): number {
  const banks = input.split("\n")

  let totalOutputJoltage = 0
  for (const bank of banks) {
    const stack: number[] = []
    const batteries = bank.split("").map(Number)

    for (let index = 0; index < batteries.length; index += 1) {
      let didPop = false
      const currentBattery = batteries[index]
      const remainingBatteries = batteries.length - index // + 1

      while (
        stack.length > 0 &&
        (stack.at(-1) ?? 0) < currentBattery &&
        stack.length + remainingBatteries > MAX_DIGITS
      ) {
        stack.pop()
        didPop = true
      }

      if (didPop || stack.length < MAX_DIGITS) {
        stack.push(currentBattery)
      }
    }

    totalOutputJoltage += Number(stack.join(""))
  }

  return totalOutputJoltage
}

export { solution }
