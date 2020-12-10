const fs = require('fs')

function findPairAddingUpTo(numbers, sum) {
  const numberDict = {};
  numbers.forEach((number) => {
    if(numberDict[number]) {
        numberDict[number] = numberDict[number] + 1;
        return;
    }
    numberDict[number] = 1;
  });
  
  for(let i = 0; i < numbers.length; i++) {
    const number = numbers[i];
    const needForSum = sum - number;

    if(numberDict[needForSum]) {
        return [number, needForSum];
    }
  }

  return [];
}

fs.readFile('input_1.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const numbers = data.trim().split("\n");

  for(let i = 0; i < numbers.length; i++) {
    const firstNumber = numbers[i];
    const needFor2020 = 2020 - firstNumber;

    const result = findPairAddingUpTo(numbers, needFor2020);

    if(result.length > 0) {
      console.log(`${firstNumber} * ${result[0]} * ${result[1]} = ${firstNumber * result[0] * result[1]}`);
      break;
    }
  };
})
