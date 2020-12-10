const fs = require('fs');

const seen = [];
function exploreMap(bagMap, lookFor) {
  let explorePointer = bagMap[lookFor];

  if(explorePointer === undefined) {
    return 0;
  }

  for(let i = 0; i < explorePointer.length; i++) {
    if(!seen.includes(explorePointer[i])) {
      exploreMap(bagMap, explorePointer[i]);
      seen.push(explorePointer[i]);
    }
  }
}

function addToMap(bagMap, rightBag1, leftBag) {
  if(rightBag1) {
    if(rightBag1 in bagMap) {
      bagMap[rightBag1].push(leftBag);
    } else {
      bagMap[rightBag1] = [leftBag];
    }
  }
}

fs.readFile('input_7.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const inputLines = data.trim().split("\n");
  
  let bagMap = {};
  for(let i = 0; i < inputLines.length; i++) {
    const containSplit = inputLines[i].split("contain");
    const leftBag = containSplit[0].split("bags")[0].trim();

    if(containSplit[1] !== " no other bags.") {
      const rightBags = containSplit[1].split(",");

      for(let j = 0; j < rightBags.length; j++) {
        const bag = rightBags[j].split("bag")[0].slice(3).trim();
        addToMap(bagMap, bag, leftBag);
      }
    }
  }

  exploreMap(bagMap, "shiny gold");
  
  console.log(`Sum is: ${seen.length}`);
})
