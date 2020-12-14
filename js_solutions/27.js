const fs = require('fs');

String.prototype.replaceAt = function(index, replacement) {
  return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}

function applyMask(number, mask) {
  const mask1 = BigInt(`0b${mask.replace(/X/g, "0")}`);
  const mask0 = BigInt(`0b${mask.replace(/X/g, "1")}`);

  return (number | mask1) & mask0;
}

fs.readFile('input_14.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  var lines = data.trim().split("\n");

  var mask;
  var numericArray = {};

  for(let i = 0; i < lines.length; i++) {
    if(lines[i].indexOf("mask") > -1) {
      mask = lines[0].split("mask = ")[1]
    } else {
      const setParts = lines[i].split(" = ");
      const address = parseInt(setParts[0].slice(4).slice(0, -1));
      const number = BigInt(setParts[1]);

      const masked = applyMask(number, mask);
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
