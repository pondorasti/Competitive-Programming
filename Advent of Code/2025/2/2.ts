function isSilly(number: Number): boolean {
  const stringified = String(number)
  const len = stringified.length

  for (let sillyLen = 1; sillyLen <= len / 2; sillyLen += 1) {
    if (len % sillyLen !== 0) continue

    const sillyChunk = stringified.slice(0, sillyLen)
    if (stringified.split(sillyChunk).length - 1 === len / sillyLen) {
      return true
    }
  }

  return false
}

function solution(input: string): number {
  const ranges = input.split(",").map((value) => value.split("-").map(Number))

  let answer = 0
  for (const [start, end] of ranges) {
    for (let id = start; id <= end; id += 1) {
      if (isSilly(id)) {
        answer += id
      }
    }
  }

  return answer
}

export { solution }
