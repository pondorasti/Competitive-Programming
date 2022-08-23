function findAnagrams(s: string, p: string): number[] {
  const answers: number[] = []
  const freq = {}

  function incrementKey(obj, key) {
    if (obj[key] === undefined) {
      obj[key] = 1
    } else {
      obj[key] += 1
    }
  }

  function decrementKey(obj, key) {
    obj[key] -= 1

    if (obj[key] === 0) {
      delete obj[key]
    }
  }

  function isEqual(lhs, rhs): boolean {
    if (Object.keys(lhs).length !== Object.keys(rhs).length) {
      return false
    }

    for (const key in lhs) {
      if (lhs[key] !== rhs[key]) return false
    }

    return true
  }

  for (const letter of p) {
    incrementKey(freq, letter)
  }

  const windowSize = p.length
  const windowFreq = {}
  for (let endWindow = windowSize - 1; endWindow < s.length; endWindow += 1) {
    if (endWindow === windowSize - 1) {
      for (let i = 0; i < windowSize; i += 1) {
        incrementKey(windowFreq, s[i])
      }
    } else {
      const prevValue = s[endWindow - windowSize]
      const newValue = s[endWindow]

      decrementKey(windowFreq, prevValue)
      incrementKey(windowFreq, newValue)
    }

    if (isEqual(freq, windowFreq)) {
      answers.push(endWindow - windowSize + 1)
    }
  }

  return answers
}
