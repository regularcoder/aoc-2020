const fs = require('fs');

// Lifted from https://stackoverflow.com/a/51562038/14084085
function modInverse(a, m) {
  // validate inputs
  [a, m] = [Number(a), Number(m)]
  if (Number.isNaN(a) || Number.isNaN(m)) {
    return NaN // invalid input
  }
  a = (a % m + m) % m
  if (!a || m < 2) {
    return NaN // invalid input
  }
  // find the gcd
  const s = []
  let b = m
  while(b) {
    [a, b] = [b, a % b]
    s.push({a, b})
  }
  if (a !== 1) {
    return NaN // inverse does not exists
  }
  // find the inverse
  let x = 1
  let y = 0
  for(let i = s.length - 2; i >= 0; --i) {
    [x, y] = [y,  x - y * Math.floor(s[i].a / s[i].b)]
  }
  return (y % m + m) % m
}

// Implementation guided by https://www.geeksforgeeks.org/chinese-remainder-theorem-set-2-implementation/
function chineseRemainder(nums, rems) {
  var prod = 1n;
  for(let i = 0; i < nums.length; i++) {
    prod *= BigInt(nums[i]);
  }

  console.log(`prod: ${prod}`);

  var pp = [];
  var inv = [];
  var number = 0n;
  for(let i = 0; i < nums.length; i++) {
    pp.push(prod / BigInt(nums[i]));
    inv.push(BigInt(modInverse(pp[i], nums[i])));

    number += BigInt(rems[i]) * pp[i] * inv[i]; 
  }

  number %= prod;
  console.log(`number: ${number}`);
}

fs.readFile('input_13.txt', 'utf8' , (err, data) => {
  if (err) {
    console.error(err)
    return
  }

  var lines = data.trim().split("\n");

  var buses = lines[1].split(",");

  var nums = [parseInt(buses[0])];
  var rems = [0];

  for(let i = 1n; i < buses.length; i++) {
    if(buses[i] !== "x") {
      const busNumber = BigInt(buses[i]);
      nums.push(busNumber);
      rems.push(busNumber - i);
    } 
  }
  chineseRemainder(nums, rems);
})
