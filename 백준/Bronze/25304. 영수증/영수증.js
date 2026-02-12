const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');

let X = Number(input[0]);
let N = Number(input[1]);
let sum = 0;

for (let i = 0; i < N; i++) {
    const arr = input[i + 2].trim().split(' ');
    sum += Number(arr[0]) * Number(arr[1]);
}

if (sum === X) {
    console.log("Yes");
} else {
    console.log("No");
}
