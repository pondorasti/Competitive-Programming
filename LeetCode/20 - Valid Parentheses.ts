function isValid(s: string): boolean {
  function isMatchingParanthesis(lhs, rhs): boolean {
    if (lhs === "(" && rhs === ")") return true
    if (lhs === "[" && rhs === "]") return true
    if (lhs === "{" && rhs === "}") return true
    return false
  }

  const stack: number[] = []
  for (let index = 0; index < s.length; index += 1) {
    if (isMatchingParanthesis(stack.at(-1), s[index])) {
      stack.pop()
    } else {
      stack.push(s[index])
    }
  }

  if (stack.length === 0) return true
  return false
}
