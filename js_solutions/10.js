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

  return {seatID, row: minRow, col: minCol};
}

fs.readFile('input_5.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const inputLines = data.trim().split("\n");
  
  let maxSeatID = 0;
  let seatMap = {};
  for(let i = 0; i < inputLines.length; i++) {
    const current = findSeat(inputLines[i]);

    seatMap[current.seatID] = current;
    if(current.seatID > maxSeatID) {
      maxSeatID = current.seatID;
    }
  }

  let mySeatID = 0;
  for(let i = 0; i < 128; i++) {
    for(let j = 0; j < 8; j++) {
      const seatID = (i * 8) + j;

      if(!(seatID in seatMap) && (seatID + 1) in seatMap && (seatID - 1) in seatMap) {
        mySeatID = seatID;
      }
    }
  }

  console.log(`My seat ID: ${mySeatID }`);
})
