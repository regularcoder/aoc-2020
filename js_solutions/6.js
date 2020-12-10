const fs = require('fs')

function countTrees(inputLines, yShift, xShift) {
  const patternLength = inputLines[0].length;

  let x = 0;
  let y = 0;
  let treeCount = 0;
  while((x + xShift) < inputLines.length) {
    // move right 3 and down 1
    x = x + xShift;
    y = (y + yShift) % patternLength;

    console.log(`x = ${x}, y = ${y}`);
    if(inputLines[x][y] === '#') {
      treeCount++;
    }
  }

  return treeCount;
}

fs.readFile('input_3.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const inputLines = data.trim().split("\n");
  
  const treeCount = countTrees(inputLines, 1, 1) * 
  countTrees(inputLines, 3, 1) * 
  countTrees(inputLines, 5, 1) *
  countTrees(inputLines, 7, 1) *
  countTrees(inputLines, 1, 2);

  console.log(`treeCount: ${treeCount}`);
})
