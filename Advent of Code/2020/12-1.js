const input = `F10
N3
F7
R90
F11
`

const instructions = input.split("\n")

function updateCoordinates(coordinates, cardinalDirection, amount) {
  if (cardinalDirection === "N") {
    coordinates.y += amount
  } else if (cardinalDirection === "S") {
    coordinates.y -= amount
  } else if (cardinalDirection === "W") {
    coordinates.x -= amount
  } else if (cardinalDirection === "E") {
    coordinates.x += amount
  }
}

function updateHeading(coordinates, angle) {
  const compassArr = ["N", "E", "S", "W"]
  const offset = angle / 90
  const currentIndex = compassArr.indexOf(coordinates.orientation)
  const nextIndex = (currentIndex + offset) % compassArr.length
  coordinates.orientation = compassArr[nextIndex]
}

function oppositeCardinalDirection(cardinalDirection) {
  if (cardinalDirection === "N") {
    return "S"
  } else if (cardinalDirection === "S") {
    return "N"
  } else if (cardinalDirection === "W") {
    return "W"
  } else if (cardinalDirection === "E") {
    return "E"
  }
}

const coordinates = {x: 0, y: 0, orientation: "E"}

for (instruction of instructions) {
  const action = instruction.substring(0, 1)
  const value = parseInt(instruction.substring(1))

  if (action === "L") {
    updateHeading(coordinates, 360 - value)
  } else if (action === "R") {
    updateHeading(coordinates, value)
  } else {
    let cardinalDirection
    if (action === "F") {
      cardinalDirection = coordinates.orientation
    } else if (action === "B") {
      cardinalDirection = oppositeCardinalDirection(coordinates.orientation)
    } else {
      cardinalDirection = action
    }
    updateCoordinates(coordinates, cardinalDirection, value)
  }
}

const ans = Math.abs(coordinates.x) + Math.abs(coordinates.y)
console.log(coordinates)
console.log(ans)
