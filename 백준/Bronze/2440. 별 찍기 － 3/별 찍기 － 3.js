const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');

let N = Number(input[0]);

for(let i = 0; i < N; i++){
    console.log('*'.repeat(N - i));
}