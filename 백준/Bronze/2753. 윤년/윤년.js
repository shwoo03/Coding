var input = require('fs').readFileSync('/dev/stdin').toString().trim().split(/\s+/);

let year = parseInt(input, 10);

let isLeap = (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
console.log(isLeap ? 1 : 0);