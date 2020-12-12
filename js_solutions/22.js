const fs = require('fs');

function searchForSeat(inputLines, istart, jstart, imove, jmove) {
  const length = inputLines[0].length;
  
  var i = istart;
  var j = jstart;
  var entry;
  do {
    i = i + imove;
    j = j + jmove;

    entry = inputLines[i] && inputLines[i][j];
  } while(entry === ".");

  return entry;
}

function applyRules(inputLines) {
  const length = inputLines[0].length;

  const newLines = [];
  var globalSet = false;
  for(let i = 0; i < inputLines.length; i++) {
    var newLine = "";
    for(let j = 0; j < length; j++) {
      const left = searchForSeat(inputLines, i, j, 0, -1);
      const right = searchForSeat(inputLines, i, j, 0, 1);
      const up = searchForSeat(inputLines, i, j, -1, 0);
      const down = searchForSeat(inputLines, i, j, 1, 0);
      const upperLeft = searchForSeat(inputLines, i, j, -1, -1);
      const upperRight = searchForSeat(inputLines, i, j, -1, 1);
      const lowerLeft = searchForSeat(inputLines, i, j, 1, -1);
      const lowerRight = searchForSeat(inputLines, i, j, 1, 1);

      const adjacent = [upperLeft, left, lowerLeft, down, lowerRight, right, upperRight, up];
      
      var set = false;
      if(inputLines[i][j] === "L") {
        if(adjacent.indexOf("#") === -1) {
          newLine += "#";
          set = true;
          globalSet = true;
        }
      }
      else if(inputLines[i][j] === "#") {
        const occupied = adjacent.filter(s => s === "#");

        if(occupied.length >= 5) {
          newLine += "L";
          set = true;
          globalSet = true;
        }
      }

      if(!set) {
        newLine += inputLines[i][j];
      }
    }

    newLines.push(newLine);
  }

  return {modified: globalSet, lines: newLines};
}

fs.readFile('input_11.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  var lines = data.trim().split("\n");
  var modified = false;

  do {
    var {modified, lines} = applyRules(lines);

    console.log();
    lines.forEach(l => console.log(l));
  } while(modified);


  const length = lines[0].length;
  var occupiedCount = 0;
  for(let i = 0; i < lines.length; i++) {
    for(let j = 0; j < length; j++) {
      if(lines[i][j] === "#") {
        occupiedCount++;
      }
    }
  }
  console.log(occupiedCount);
})
