const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');

// S = (R1 + R2) / 2
// R2 = 2S - R1

let [R1, S] = input[0].split(' ').map(Number);

let R2 = 2 * S - R1;

console.log(R2);