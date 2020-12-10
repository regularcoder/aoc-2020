const fs = require('fs');

fs.readFile('input_9.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const inputLines = data.trim().split("\n");
  
  const numberToFind = 507622668;

  for(let i = 0; i < inputLines.length; i++) {
    const currentStart = parseInt(inputLines[i]);

    let runningSum = 0;
    let smallest = currentStart;
    let largest = currentStart;
    for(let j = i; j < inputLines.length; j++) {
      const currentNumber = parseInt(inputLines[j]);

      if(currentNumber === numberToFind) {
        continue;
      }

      runningSum += currentNumber;

      if(currentNumber > largest) {
        largest = currentNumber;
      }

      if(currentNumber < smallest) {
        smallest = currentNumber;
      }

      if(runningSum === numberToFind) {
        console.log(`largest: ${largest}, smallest: ${smallest}, sum is ${largest + smallest}`);
        break;
      } else if (j > numberToFind) {
        break;
      }
    }
  }
})
