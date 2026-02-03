var input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let T = input[0];
let output = [];

for(let i = 0; i < T; i++){
    const line = input[i+1].split(' ').map(Number);
    output.push(line[0] + line[1]);
}

console.log(output.join('\n'));