const fs = require('fs');

fs.readFile('input_13.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  var lines = data.trim().split("\n");

  var timestamp = parseInt(lines[0]);
  var buses = lines[1].split(",");
  
  var smallestStartingPoint;
  var smallestBusNo;
  for(let i = 0; i < buses.length; i++) {
    if(buses[i] !== "x") {
      const busNumber = parseInt(buses[i]);
      const startingPoint = Math.floor(timestamp/busNumber) * busNumber;
      const postStartPoint = timestamp - (startingPoint + busNumber);

      if(smallestStartingPoint === undefined || smallestStartingPoint < postStartPoint) {
        smallestStartingPoint = postStartPoint;
        smallestBusNo = busNumber;
      }
    } 
  }

  const answer = Math.abs(smallestStartingPoint) * smallestBusNo;
  console.log(`${smallestBusNo} starts at ${smallestStartingPoint}, answer: ${answer}`);
})
