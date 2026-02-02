var input = require('fs').readFileSync('/dev/stdin').toString().trim().split(/\s+/);

let N = Number(input[0]);

let result = 0;
for(let i = 0; i < N; i++){
    let num = input[1][i];
    result += Number(num);
}

console.log(result);