const fs = require('fs')

fs.readFile('input_1.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const numbers = data.split("\n");

  const numberDict = {};
  numbers.forEach((number) => {
    if(numberDict[number]) {
        numberDict[number] = numberDict[number] + 1;
        return;
    }
    numberDict[number] = 1;
  });
  
  numbers.forEach((number) => {
    const needFor2020 = 2020 - number;

    if(numberDict[needFor2020]) {
        console.log(`${number} * ${needFor2020} = ${number * needFor2020}`);
    }
  });
})
