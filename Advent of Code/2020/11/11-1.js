const input = `L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL`

function duplicateArr(arr) {
  let newArr = []
  for (index in arr) {
    newArr[index] = arr[index].slice()
  }

  return newArr
}

function displayGrid(grid) {
  let displayGrid = duplicateArr(grid)

  for (row in displayGrid) {
    displayGrid[row] = displayGrid[row].join("")
  }
  displayGrid = displayGrid.join("\n")

  console.log(displayGrid)
  console.log()
}

function compareGrids(lhs, rhs) {
  for (row in grid) {
    for (column in grid[row]) {
      if (lhs[row][column] !== rhs[row][column]) {
        return false
      }
    }
  }

  return true
}

let grid = input.split("\n")
for (index in grid) {
  grid[index] = grid[index].split("")
}

let isDifferent = true
const directionsX = [1, -1, 0, 0, 1, -1, 1, -1]
const directionsY = [0, 0, 1, -1, 1, -1, -1, 1]
while (isDifferent) {
  let newGrid = duplicateArr(grid)
  for (row in grid) {
    for (column in grid[row]) {
      let occupiedSeats = 0
      for (seatIndex in directionsX) {
        let adjacentX = parseInt(column) + directionsX[seatIndex]
        let adjacentY = parseInt(row) + directionsY[seatIndex]
        if (
          0 <= adjacentX &&
          adjacentX < grid[row].length &&
          0 <= adjacentY &&
          adjacentY < grid.length &&
          grid[adjacentY][adjacentX] === "#"
        ) {
          occupiedSeats += 1
        }
      }

      if (grid[row][column] === "L" && occupiedSeats === 0) {
        newGrid[row][column] = "#"
      } else if (grid[row][column] === "#" && occupiedSeats >= 4) {
        newGrid[row][column] = "L"
      } else {
        newGrid[row][column] = grid[row][column]
      }
    }
  }

  isDifferent = !compareGrids(newGrid, grid)
  grid = newGrid
}

let openSeats = 0
for (row in grid) {
  for (column in grid[row]) {
    if (grid[row][column] === "#") {
      openSeats += 1
    }
  }
}

displayGrid(grid)
console.log(openSeats)
