const fs = require('fs');

function applyRules(inputLines) {
  const length = inputLines[0].length;

  const newLines = [];
  var globalSet = false;
  for(let i = 0; i < inputLines.length; i++) {
    var newLine = "";
    for(let j = 0; j < length; j++) {
      const left = inputLines[i][j - 1];
      const right = inputLines[i][j + 1];
      const up = inputLines[i - 1] && inputLines[i - 1][j];
      const down = inputLines[i + 1] && inputLines[i + 1][j];
      const upperLeft = inputLines[i - 1] && inputLines[i - 1][j - 1];
      const upperRight = inputLines[i - 1] && inputLines[i - 1][j + 1];
      const lowerLeft = inputLines[i + 1] && inputLines[i + 1][j - 1];
      const lowerRight = inputLines[i + 1] && inputLines[i + 1][j + 1];

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

        if(occupied.length >= 4) {
          console.log(`[${i}][${j}], adjacent: ${adjacent}`);
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
