const fs = require('fs')

function checkValidity(password, charToLookFor, min, max) {
    let count = 0;
    
    if(password[min - 1] === charToLookFor) {
      count++;
    }
    
    if(password[max - 1] === charToLookFor) {
      count++;
    }

    return count === 1;
}

fs.readFile('input_3.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const inputLines = data.trim().split("\n");
  
  const patternLength = inputLines[0].length;

  let x = 0;
  let y = 0;
  let treeCount = 0;
  while((x + 1) < inputLines.length) {
    // move right 3 and down 1
    x = x + 1;
    y = (y + 3) % patternLength;

    console.log(`x = ${x}, y = ${y}`);
    if(inputLines[x][y] === '#') {
      treeCount++;
    }
  }

  console.log(`treeCount: ${treeCount}`);
})
