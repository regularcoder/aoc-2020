const fs = require('fs');

fs.readFile('input_10.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  const inputLines = data.trim().split("\n");
  const intLines = inputLines.map(x => parseInt(x)).sort((a, b) => a - b);

  var current = 0;
  var diff1 = 0;
  var diff3 = 1;

  for(let i = 0; i < intLines.length; i++) {
    const diff = intLines[i] - current;
    console.log(`${i} --> ${intLines[i]}, ${intLines[i]} - ${current} = ${diff}`);

    if(diff === 1) {
      diff1++;
    } else if(diff === 3) {
      diff3++;
    }

    current = intLines[i];
  }

  console.log(`diff1: ${diff1}, diff3: ${diff3}, diff1 * diff3 = ${diff1 * diff3}`);
})
