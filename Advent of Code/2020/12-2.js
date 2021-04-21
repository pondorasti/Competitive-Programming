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
  const compassArr = ["E", "S", "W", "N"]
  const offset = angle / 90
  const currentIndex = compassArr.indexOf(coordinates.orientation)
  const nextIndex = (currentIndex + offset) % compassArr.length
  coordinates.orientation = compassArr[nextIndex]

  for (let i = 0; i < offset; ++i) {
    const oldX = coordinates.x
    coordinates.x = coordinates.y
    coordinates.y = -oldX
  }
}

function updateShip(coordinates, waypoint, value) {
  coordinates.x += waypoint.x * value
  coordinates.y += waypoint.y * value
}

const waypoint = {x: 10, y: 1, baseX: 10, baseY: 1, orientation: "E"}
const ship = { x: 0, y: 0 }

for (instruction of instructions) {
  const action = instruction.substring(0, 1)
  const value = parseInt(instruction.substring(1))

  if (action === "L") {
    updateHeading(waypoint, 360 - value)
  } else if (action === "R") {
    updateHeading(waypoint, value)
  } else if (action === "F") {
    updateShip(ship, waypoint, value)
  } else {
    updateCoordinates(waypoint, action, value)
  }
}

const ans = Math.abs(ship.x) + Math.abs(ship.y)
console.log(ship)
console.log(ans)
