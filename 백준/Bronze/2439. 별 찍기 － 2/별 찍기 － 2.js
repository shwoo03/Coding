var input = require('fs').readFileSync('/dev/stdin').toString().trim().split(/\s+/).map(Number);

let N = input[0];

for(let i = N; i > 0; i--){
    console.log(" ".repeat(i-1) + "*".repeat(N - i + 1))
}