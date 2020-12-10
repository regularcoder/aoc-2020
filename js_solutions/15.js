const fs = require('fs');


fs.readFile('input_8.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const inputLines = data.trim().split("\n");
  
  let seenInstructions = {};
  let i = 0;
  let accumulator = 0;
  while(true) {
    const [instruction, argument] = inputLines[i].split(" ");
    console.log(`Instruction ${instruction} and arg ${argument}`);

    if(i in seenInstructions) {
      console.log(`DUPLICATE! ${i}, accumulator is ${accumulator}`);
      break;
    } else {
      seenInstructions[i] = true;
    }

    switch(instruction) {
      case 'nop':
        console.log(`nop`);
        i++;
        break;

      case 'acc':
        console.log(`acc`);
        accumulator = accumulator + parseInt(argument);
        i++;
        break;    

      case 'jmp':
        i = i + parseInt(argument);
        console.log(`jmp to ${i} after adding ${parseInt(argument)}`);
        break;  
    }
  }

  const sum = 0;
  
  console.log(`Sum is: ${sum}`);
})
