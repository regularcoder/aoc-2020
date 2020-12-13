const fs = require('fs');
const { start } = require('repl');

function* generateSchedule(busNumber) {
  var current = 0;
  while (true) {
    yield busNumber;
    current += busNumber;
  }
}

fs.readFile('input_13.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  var lines = data.trim().split("\n");

  var buses = lines[1].split(",");
  var departureMap = {};
  var largest = 0;

  var starting = {
    busNumber: parseInt(buses[0]),
    run: parseInt(buses[0]),
  };
  for(let i = 1; i < buses.length; i++) {
    if(buses[i] !== "x") {
      const busNumber = parseInt(buses[i]);

      departureMap[i] = {
        busNumber,
        run: busNumber + i,
      };
      largest = i;
    } 
  }

  var sequential = false;
  var ctr = 0;
  while(!sequential) {
    starting.run += starting.busNumber;

    ctr++;
    console.log();
    console.log(departureMap);

    // console.log(`smallest: ${starting.run}, largest ${departureMap[largest].run}`);
    sequential = true;
    for (const [key, value] of Object.entries(departureMap)) {

      const startingPoint = Math.floor(starting.run/value.busNumber) * value.busNumber;
      const postStartPoint = startingPoint + value.busNumber;

      // console.log(`For ${value.busNumber}, closest is ${postStartPoint}, diff is ${postStartPoint - starting.run}, should be ${key}`);
      if(postStartPoint - starting.run != key) {
        sequential = false;
        break;
      }
    }
  }
  console.log();
  console.log(`${starting.run} in ${ctr} iterations`);

})
