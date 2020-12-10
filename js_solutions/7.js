const fs = require('fs')

function checkValidity(line) {
  const splitFields = line.split(" ");

  let mandatoryCount = 0;
  let cidFound = false;
  for(let i = 0; i < splitFields.length; i++) {
    const fieldDataLine = splitFields[i].split(":");
    const fieldName = fieldDataLine[0];
    const fieldData = fieldDataLine[1];

    if(fieldName === "byr" || 
    fieldName === "iyr" || 
    fieldName === "eyr" ||
    fieldName === "hgt" || 
    fieldName === "hcl" || 
    fieldName === "ecl" || 
    fieldName === "pid" || 
    fieldName === "cid") {
      mandatoryCount++;

      if(fieldName === "cid") {
        cidFound = true;
      }
    }
  }

  return (mandatoryCount === 8 || (mandatoryCount === 7 && !cidFound));
}

function countValid(inputLines) {

  let i = 0;
  let validCount = 0;
  while(i < inputLines.length) {    
    let line = inputLines[i];

    while(i+1 < inputLines.length && inputLines[i+1] !== "") {
      i++;
      line += " " + inputLines[i];
    }

    i++;
    
    if(checkValidity(line)) {
      validCount++;
    }
  }

  return validCount;
}

fs.readFile('input_4.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const inputLines = data.trim().split("\n");
  
  const treeCount = countValid(inputLines);

  console.log(`validCount: ${treeCount}`);
})
