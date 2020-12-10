const fs = require('fs')

function findSeat(inputLine) {
  let minRow = 0;
  let maxRow = 127;

  for(let i = 0; i < 7; i++) {
    const halfWay = Math.floor((maxRow + minRow) / 2);
    if(inputLine[i] === "F") {
      maxRow = halfWay;
    } else {
      minRow = halfWay + 1;
    }
  }

  let minCol = 0;
  let maxCol = 7;

  for(let i = 7; i < 10; i++) {
    const halfWay = Math.floor((maxCol + minCol) / 2);
    if(inputLine[i] === "L") {
      maxCol = halfWay;
    } else {
      minCol = halfWay + 1;
    }
  }

  const seatID = (minRow * 8) + minCol;

  return seatID;
}

fs.readFile('input_5.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const inputLines = data.trim().split("\n");
  
  let maxSeatID = 0;
  for(let i = 0; i < inputLines.length; i++) {
    const current = findSeat(inputLines[i]);
    if(current > maxSeatID) {
      maxSeatID = current;
    }
  }

  console.log(`MAX: ${maxSeatID}`);
})
