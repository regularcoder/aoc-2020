const fs = require('fs');

function checkSum(numberToFind, runningArray) {
  let numberMap = {};
  for(let i = 0; i < runningArray.length; i++) {
    numberMap[runningArray[i]] = true;
  }

  for(let i = 0; i < runningArray.length; i++) {
    // runningArray[i] + anything should be = numberToFind
    const needed = numberToFind - runningArray[i];

    if(needed in numberMap) {
      return true;
    }
  }

  return false;
}

fs.readFile('input_9.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const inputLines = data.trim().split("\n");
  
  const preamble = 25;
  const runningArray = [];
  for(let i = 0; i < inputLines.length; i++) {
    const number = parseInt(inputLines[i]);

    if(runningArray.length === preamble) {
      console.log(`Check if ${number} is in ${JSON.stringify(runningArray)}`);

      if(!checkSum(number, runningArray)) {
        console.log(`${number} sum not in ${JSON.stringify(runningArray)}`);
        break;
      }

      runningArray.shift();
    }

    runningArray.push(number);
        
    console.log(`${JSON.stringify(runningArray)} <---- ${number}`);
  }
})
