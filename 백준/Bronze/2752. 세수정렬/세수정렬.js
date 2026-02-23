const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split(' ').map(Number);

input.sort((a, b) => a - b);

console.log(input.join(' '));