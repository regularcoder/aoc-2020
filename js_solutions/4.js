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

fs.readFile('input_2.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const passwordLines = data.trim().split("\n");

  let validCount = 0;
  for(let i = 0; i < passwordLines.length; i++) {
    const passwordLine = passwordLines[i];

    const passwordSplit = passwordLine.split(' ');
    
    const password = passwordSplit[2];
    const charToLookFor = passwordSplit[1][0];
    const minMax = passwordSplit[0].replace(':', '').split('-')
    const min = minMax[0];
    const max = minMax[1];

    if(checkValidity(password, charToLookFor, min, max)) {
        validCount++;
        console.log(`VALID password: ${password}, charToLookFor: ${charToLookFor}, min: ${min}, max: ${max}`);
    }
  };

  console.log(`validCount: ${validCount}`);
})
