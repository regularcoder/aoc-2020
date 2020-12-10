const fs = require('fs');

function exploreMap(bagMap, lookFor) {

  let explorePointer = bagMap[lookFor];

  if(explorePointer === undefined) {
    return 0;
  }

  let count = 0;
  for(let i = 0; i < explorePointer.length; i++) {
      const innerCount = exploreMap(bagMap, explorePointer[i].bagName);

      count += (explorePointer[i].count * innerCount) + explorePointer[i].count;
  }
  return count;
}

function addToMap(bagMap, rightBag, leftBag) {
  if(leftBag) {
    if(leftBag in bagMap) {
      bagMap[leftBag].push(rightBag);
    } else {
      bagMap[leftBag] = [rightBag];
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
        const bagSplit = rightBags[j].split("bag")[0].trim().split(" ");
        const bagName = bagSplit[1] + " " + bagSplit[2];
        const bag = {
          bagName,
          count: parseInt(bagSplit[0]),
        };
        addToMap(bagMap, bag, leftBag);
      }
    }
  }

  const sum = exploreMap(bagMap, "shiny gold");
  
  console.log(`Sum is: ${sum}`);
})
