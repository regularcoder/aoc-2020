const fs = require('fs');

function processInstruction(instruction, argument) {
  switch(instruction) {
    case 'nop':
      return 1;

    case 'acc':
      return 1;

    case 'jmp':
      return parseInt(argument);
  }
}

function runLoop(inputLines, instructionToVary) {
  let seenInstructions = {};
  let i = 0;
  let accumulator = 0;

  while(true) {
    if(i >= inputLines.length) {
      console.log(`accumulator is ${accumulator}`);
      return {status: true, seenInstructions};
    }
    let [instruction, argument] = inputLines[i].split(" ");
    console.log(`${i} Instruction ${instruction} and arg ${argument}`);


    if(i === instructionToVary) {
      if(instruction === "jmp") {
        instruction = "nop";
      } else if(instruction === "nop") {
        instruction = "jmp";
      }
      console.log(`Instruction modified to ${instruction} and arg ${argument}`);
    }


    if(i in seenInstructions) {
      console.log(`DUPLICATE! ${i}, accumulator is ${accumulator}`);
      return {status: false, seenInstructions};
    } else {
      seenInstructions[i] = true;
    }

    if(instruction === "acc") {
      accumulator = accumulator + parseInt(argument);
    }

    i += processInstruction(instruction, argument);
  }
}


fs.readFile('input_8.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const inputLines = data.trim().split("\n");
  
  const {status, seenInstructions} = runLoop(inputLines);

  for (const [key, value] of Object.entries(seenInstructions)) {
    console.log(`Varying ${key}`);
    const {status} = runLoop(inputLines, parseInt(key));

    if(status) {
      console.log("FOUND FOUND FOUND!!!");
      break;
    };
  }
})
