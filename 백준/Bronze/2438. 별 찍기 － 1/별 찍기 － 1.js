var input = require('fs').readFileSync('/dev/stdin').toString().trim().split(/\s+/);

let N = parseInt(input[0]);

for(let i = 1; i <= N; i++){
    console.log('*'.repeat(i));
}