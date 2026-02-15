const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');

let arr = [];
arr = input[0].split(' ').map(Number);
arr.sort((a, b) => a - b);

console.log(arr[1]);
