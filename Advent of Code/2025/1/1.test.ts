import { describe, expect, test } from "bun:test"
import { solution } from "./1"

const INPUT = await Bun.file("./Advent of Code/2025/1/input.txt").text()
const EXAMPLE_INPUT = `L68
L30
R48
L5
R60
L55
L1
L99
R14
L82`

describe("Year 2025, Day 1, Part 1", () => {
  test("Example", () => {
    expect(solution(EXAMPLE_INPUT)).toEqual(3)
  })

  test("Input", () => {
    expect(solution(INPUT)).toEqual(1165)
  })
})
