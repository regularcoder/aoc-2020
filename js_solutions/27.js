const fs = require('fs');

String.prototype.replaceAt = function(index, replacement) {
  return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}

function applyMask(number, mask) {
  var binaryNumber = number.toString(2).padStart(36, "0");

  console.log(`pre binaryNumber: ${binaryNumber}`);
  mask.forEach((maskedDigit) => {
    binaryNumber = binaryNumber.replaceAt(maskedDigit.index, maskedDigit.value);
  });
  console.log(`pos binaryNumber: ${binaryNumber}`);

  return BigInt(`0b${binaryNumber}`);
}

fs.readFile('input_14.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  var lines = data.trim().split("\n");

  var mask;
  var maskChars;
  var numericArray = {};

  for(let i = 0; i < lines.length; i++) {
    if(lines[i].indexOf("mask") > -1) {
      mask = lines[0].split("mask = ")[1]

      maskChars = [];
      for(var j = mask.length - 1; j >= 0; j--) {
        if(mask[j] != "X") {
          maskChars.push({index: j, value: mask[j]});
        }
      }
      console.log(maskChars);
    } else {
      const setParts = lines[i].split(" = ");
      const address = parseInt(setParts[0].slice(4).slice(0, -1));

      const number = BigInt(setParts[1]);

      const masked = applyMask(number, maskChars);
  
      numericArray[address] = masked;
      console.log(`number: ${number}, address = ${address}, masked: ${masked}`);
    }
  }

  var sum = 0n;
  for (const [key, value] of Object.entries(numericArray)) {
    sum += value;
  }

  console.log(sum);
})
