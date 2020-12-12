const fs = require('fs');

fs.readFile('input_12.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  var lines = data.trim().split("\n");
  
  var x = 0;
  var y = 0;
  var wx = 10;
  var wy = 1;
  for(let i = 0; i < lines.length; i++) {   
    var instruction = lines[i][0];
    var distance = parseInt(lines[i].slice(1));

    const numTurns = distance / 90;
    switch(instruction) {
      case "F":  
        const xshift = (distance * wx);
        const yshift = (distance * wy);

        x += xshift;
        y += yshift; 
        break;

      case "N":
        wy += distance;
        break;

      case "S":
        wy -= distance;
        break;

      case "W":
        wx -= distance;
        break;

      case "E":
        wx += distance;
        break;

      case "R":
        for(let j = 0; j < numTurns; j++) {
          [wx, wy] = [wy, wx]
          wy *= -1;
        }
        break;

      case "L":
        for(let j = 0; j < numTurns; j++) {
          [wx, wy] = [wy, wx]
          wx *= -1;
        }
        break;
    }    
  }

  const result = Math.abs(x) + Math.abs(y);
  console.log(`FINAL x: ${x}, y: ${y}, wx: ${wx}, wy: ${wy} result: ${result}`);    
})
