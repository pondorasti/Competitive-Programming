import { describe, expect, test } from "bun:test"
import { solution } from "./1"

const INPUT = await Bun.file("./Advent of Code/2025/3/input.txt").text()
const EXAMPLE_INPUT = `987654321111111
811111111111119
234234234234278
818181911112111`

describe("Year 2025, Day 3, Part 1", () => {
  test("Example", () => {
    expect(solution(EXAMPLE_INPUT)).toEqual(357)
  })

  test("Input", () => {
    expect(solution(INPUT)).toEqual(17330)
  })
})
