const fs = require('fs')

function countDistinct(inputLine) {
  let charMap = {};
  for(let i = 0; i < inputLine.length; i++) {
    if(inputLine[i] >= 'a' && inputLine[i] <= 'z') {
      charMap[inputLine[i]] = true;
    }
  }

  return Object.keys(charMap).length;
}

fs.readFile('input_6.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const inputLines = data.trim().split("\n\n");
  
  let sum = 0;
  for(let i = 0; i < inputLines.length; i++) {
    sum += countDistinct(inputLines[i]);
  }
  
  console.log(`Sum is: ${sum}`);
})
