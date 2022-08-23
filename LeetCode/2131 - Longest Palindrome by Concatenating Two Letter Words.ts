function longestPalindrome(words: string[]): number {
  function reverseString(str: string): string {
    return `${str[1]}${str[0]}`
  }

  let ans = 0

  let sameLetterPairs = 0
  const freq = new Map()

  for (let word of words) {
    const value = freq.get(word)

    const reversedWord = reverseString(word)
    const reversedValue = freq.get(reversedWord)

    if (reversedValue > 0) {
      freq.set(reversedWord, reversedValue - 1)
      ans += 4
    } else {
      freq.set(word, value + 1 || 1)
    }
  }

  console.log({ freq, ans })
  for (let [key, val] of freq) {
    if (key === reverseString(key) && val > 0) {
      ans += 2
      break
    }
  }

  return ans
}
