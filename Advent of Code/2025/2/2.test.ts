import { describe, expect, test } from "bun:test"
import { solution } from "./2"

const INPUT = await Bun.file("./Advent of Code/2025/2/input.txt").text()
const EXAMPLE_INPUT = `11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124`

describe("Year 2025, Day 2, Part 2", () => {
  test("Example", () => {
    expect(solution(EXAMPLE_INPUT)).toEqual(4174379265)
  })

  test("Input", () => {
    expect(solution(INPUT)).toEqual(65794984339)
  })
})
