const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');

let sum = 0;

for(let i = 0; i < input.length; i++) {
    let num = parseInt(input[i]);

    if(num < 40){
        sum += 40;
    }else{
        sum += num;
    }
}

console.log(sum / 5);