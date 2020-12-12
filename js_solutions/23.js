const fs = require('fs');

fs.readFile('input_12.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  var lines = data.trim().split("\n");
  
  var xmov;
  var ymov;
  var x = 0;
  var y = 0;
  var currDirection = 1;
  var directions = "NESW";
  for(let i = 0; i < lines.length; i++) {
    console.log();    
    console.log(`x: ${x}, y: ${y}, direction: ${directions[currDirection]}`);    

    var instruction = lines[i][0];
    var distance = parseInt(lines[i].slice(1));

    switch(directions[currDirection]) {
      case "E":
        xmov = 1;
        ymov = 0;
        break;

      case "S":
        xmov = 0;
        ymov = -1;
        break;

      case "W":
        xmov = -1;
        ymov = 0;
        break;

      case "N":
        xmov = 0;
        ymov = 1;
        break;
    }

    const numTurns = distance / 90;
    switch(instruction) {
      case "F":
        x += (distance * xmov);
        y += (distance * ymov);
        break;

      case "N":
        y += distance;
        break;

      case "S":
        y -= distance;
        break;

      case "W":
        x -= distance;
        break;

      case "E":
        x += distance;
        break;

      case "R":
        currDirection = Math.abs((currDirection + numTurns)) % directions.length;

        console.log(`${instruction}${distance} means I am now facing ${directions[currDirection]}`);
        break;

      case "L":
        currDirection = (currDirection - numTurns) % directions.length;

        console.log(`currDirection: ${currDirection}`);
        if(currDirection < 0) {
          currDirection = directions.length + currDirection;
          console.log(`currDirection: ${currDirection}`);
        }

        console.log(`${instruction}${distance} means I am now facing ${directions[currDirection]}`);
        break;
    }
    
    console.log(`${instruction} --- ${distance}`);
  }

  const result = Math.abs(x) + Math.abs(y);
  console.log(`FINAL x: ${x}, y: ${y}: result: ${result}`);    
})
