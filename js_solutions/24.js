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
  var wx = 10;
  var wy = 1;
  var currDirection = 1;
  var directions = "NESW";
  for(let i = 0; i < lines.length; i++) {   
    var instruction = lines[i][0];
    var distance = parseInt(lines[i].slice(1));

    switch(directions[currDirection]) {
      case "E":
        xmov = 1;
        ymov = 1;
        break;

      case "S":
        xmov = 1;
        ymov = -1;
        break;

      case "W":
        xmov = -1;
        ymov = -1;
        break;

      case "N":
        xmov = -1;
        ymov = 1;
        break;
    }

    console.log();    
    console.log(`${instruction} --- ${distance}`);
    console.log(`Pre: x: ${x}, y: ${y}, direction: ${directions[currDirection]}`); 
    console.log(`Pre: wx: ${wx * xmov}, wy: ${wy * ymov}`);    

    const numTurns = distance / 90;
    switch(instruction) {
      case "F":  
        const xshift = (distance * wx * xmov);
        const yshift = (distance * wy * ymov);
          console.log(`Fx ${x} += ${xshift}`);   
          console.log(`Fy ${y} += ${yshift}`); 

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
        currDirection = Math.abs((currDirection + numTurns)) % directions.length;

        if(numTurns % 2 !== 0) {
          console.log(`Swapping`);
          [wx, wy] = [wy, wx]
        }

        console.log(`${instruction}${distance} means I am now facing ${directions[currDirection]}`);
        break;

      case "L":
        currDirection = (currDirection - numTurns) % directions.length;

        if(numTurns % 2 !== 0) {
          console.log(`Swapping`);
          [wx, wy] = [wy, wx]
        }

        console.log(`currDirection: ${currDirection}`);
        if(currDirection < 0) {
          currDirection = directions.length + currDirection;
          console.log(`currDirection: ${currDirection}`);
        }

        console.log(`${instruction}${distance} means I am now facing ${directions[currDirection]}`);
        break;
    }    

    console.log(`Post: x: ${x}, y: ${y}, direction: ${directions[currDirection]}`); 
  }

  const result = Math.abs(x) + Math.abs(y);
  console.log(`FINAL x: ${x}, y: ${y}, wx: ${wx * xmov}, wy: ${wy * ymov} result: ${result}`);    
})
