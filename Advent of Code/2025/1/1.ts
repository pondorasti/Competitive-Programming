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
    position = (position + normalizedDistance) % 100

    if (position === 0) zeroAppearances += 1
  }

  return zeroAppearances
}

export { solution }
