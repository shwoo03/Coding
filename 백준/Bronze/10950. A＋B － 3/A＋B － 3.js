var input = require('fs').readFileSync('/dev/stdin').toString().trim().split(/\s+/).map(Number);

let N = input[0];
let idx = 1;
let out = [];

for(let i = 0; i < N; i++){
    let a = input[idx++];
    let b = input[idx++];
    out.push(a + b);
}

console.log(out.join('\n'));