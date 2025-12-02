function solution(input: string): number {
  const rotations = input.split("\n").map((rawRotation) => {
    const direction = rawRotation[0]
    const distance = Number(rawRotation.slice(1, rawRotation.length))
    const normalizedDistance = (() => {
      if (direction === "L") return -1 * distance
      return distance
    })()
    return { direction, distance, normalizedDistance }
  })

  let position = 50
  let zeroAppearances = 0
  for (const { normalizedDistance } of rotations) {
    position = position + normalizedDistance

    console.log("--------------------------")
    if (position < 0 || position > 100) {
      console.log({ floor: Math.abs(Math.floor(position / 100)), partial: position })
      zeroAppearances += Math.abs(Math.floor(position / 100))
      if (position - normalizedDistance === 0) {
        zeroAppearances -= 1
      }
    }

    position %= 100
    if (position < 0) position += 100
    console.log({ position })

    if (position === 0) zeroAppearances += 1
    console.log({ zeroAppearances })
    console.log("--------------------------")
  }

  return zeroAppearances
}

export { solution }
