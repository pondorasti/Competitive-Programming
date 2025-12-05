import { describe, expect, test } from "bun:test"
import { solution } from "./2"

const INPUT = await Bun.file("./Advent of Code/2025/3/input.txt").text()
const EXAMPLE_INPUT = `987654321111111
811111111111119
234234234234278
818181911112111`

describe("Year 2025, Day 3, Part 2", () => {
  test("Example", () => {
    expect(solution(EXAMPLE_INPUT)).toEqual(3121910778619)
  })

  test("Input", () => {
    expect(solution(INPUT)).toEqual(171518260283767)
  })
})
