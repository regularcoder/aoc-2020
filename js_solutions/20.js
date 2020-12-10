const fs = require('fs');

let cache = {};
function moveForward(joltMap, intLines, defaultCurrent = undefined) {
  var path = [];
  var foundPaths = 1;

  if(defaultCurrent in cache) {
    return cache[defaultCurrent];
  }

  var current = 0;
  if(defaultCurrent) {
    current = defaultCurrent;
  }
  const max = intLines[intLines.length - 1];
  while(current !== max) {
    var found = false;
    const prev1 = current + 1;
    const prev2 = current + 2;
    const prev3 = current + 3;

    path.push(current);

    if(prev1 in joltMap) {
      current = prev1;
      found = true;
    }

    if(prev2 in joltMap) {
      if(!found) {
        current = prev2;
      } else {
        const move2 = moveForward(joltMap, intLines, prev2);
        foundPaths += move2;
      }
    }

    if(prev3 in joltMap) {
      if(!found) {
        current = prev3;
      } else {
        const move3 = moveForward(joltMap, intLines, prev3);
        foundPaths += move3;
      }
    }
  }

  path.push(max);

  cache[defaultCurrent] = foundPaths;
  return foundPaths;
}

fs.readFile('input_10.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const inputLines = data.trim().split("\n");
  const intLines = inputLines.map(x => parseInt(x)).sort((a, b) => a - b);

  // Build map
  var joltMap = {};
  for(let i = 0; i < intLines.length; i++) {
    joltMap[intLines[i]] = 0;
  }

  const foundPaths = moveForward(joltMap, intLines);

  console.log(`foundPaths: ${foundPaths}`);
})
