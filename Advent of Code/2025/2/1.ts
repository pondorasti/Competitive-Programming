function twiceChecker(number: Number): boolean {
  const stringified = String(number)
  const len = stringified.length

  if (len % 2 !== 0) return false
  return stringified.slice(0, len / 2) === stringified.slice(len / 2, len)
}

function solution(input: string): number {
  const ranges = input.split(",").map((value) => value.split("-").map(Number))

  let answer = 0
  for (const [start, end] of ranges) {
    for (let id = start; id <= end; id += 1) {
      if (twiceChecker(id)) {
        answer += id
      }
    }
  }

  return answer
}

export { solution }
