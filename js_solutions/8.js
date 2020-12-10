const fs = require('fs')

function checkNumber(number, min, max) {
  return (number >= min && number <= max);
}

function checkHeight(height) {
  let heightSplit;
  if(height.indexOf("in") > -1) {
    heightSplit = height.split("in");
    return checkNumber(heightSplit[0], 59, 76);
  } else {
    heightSplit = height.split("cm");    
    return checkNumber(heightSplit[0], 150, 193);
  }
}

function checkHairColour(colour) {
  return /^#[0-9a-f]{6}$/.test(colour);
}

function checkEyeColour(colour) {
  return colour === "amb" || 
  colour === "blu" || 
  colour === "brn" || 
  colour === "gry" || 
  colour === "grn" || 
  colour === "hzl" || 
  colour === "oth";
}

function checkPassport(colour) {
  return /^0*[0-9]{9}$/.test(colour);
}

function checkFieldValidity(fieldName, fieldValue) {
  switch(fieldName) {
    case "byr":
      return checkNumber(fieldValue, 1920, 2002);
    
    case "iyr":
      return checkNumber(fieldValue, 2010, 2020);
    
    case "eyr":
      return checkNumber(fieldValue, 2020, 2030);
    
    case "hgt":
      return checkHeight(fieldValue);
    
    case "hcl":
      return checkHairColour(fieldValue);
    
    case "ecl":        
      return checkEyeColour(fieldValue);
    
    case "pid":        
      return checkPassport(fieldValue);

    default:
      return true;
  }

  return fieldValid;
}

function checkLineValidity(line) {
  const splitFields = line.split(" ");

  let mandatoryCount = 0;
  let cidFound = false;
  let fieldValid = true;
  for(let i = 0; i < splitFields.length; i++) {
    fieldValid = true;

    const fieldDataLine = splitFields[i].split(":");
    const fieldName = fieldDataLine[0];
    const fieldValue = fieldDataLine[1];

    if(fieldName === "byr" || 
    fieldName === "iyr" || 
    fieldName === "eyr" ||
    fieldName === "hgt" || 
    fieldName === "hcl" || 
    fieldName === "ecl" || 
    fieldName === "pid" || 
    fieldName === "cid") {
      if(fieldName === "cid") {
        cidFound = true;
      }

      if(!checkFieldValidity(fieldName, fieldValue)) {
        break;
      }

      mandatoryCount++;
    }
  }

  return fieldValid && (mandatoryCount === 8 || (mandatoryCount === 7 && !cidFound));
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
    
    if(checkLineValidity(line)) {
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
