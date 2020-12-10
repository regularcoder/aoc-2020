const fs = require('fs')

function countDistinct(inputLine) {
  let charMap = {};

  for(let i = 0; i < inputLine.length; i++) {
    const char = inputLine[i];
    if(char >= 'a' && char <= 'z') {
      if(char in charMap) {
        charMap[char] = charMap[char] + 1;
      } else {
        charMap[char] = 1;
      }
    }
  }

  const numPeople = inputLine.split("\n").length;

  let vote = 0;
  for (const [key, value] of Object.entries(charMap)) {
    if(value === numPeople) {
      vote++;
    }
  }

  return vote;
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
