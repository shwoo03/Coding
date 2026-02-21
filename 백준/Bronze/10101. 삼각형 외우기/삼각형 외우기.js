const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');

const [a, b, c] = input.map(Number);

if ((a+b+c) === 180 && a === b && b === c) {
    console.log("Equilateral");
}else if( (a+b+c) == 180 && (a === b || b === c || a === c)){
    console.log("Isosceles");
}else if((a+b+c) == 180){
    console.log("Scalene");
}else{
    console.log("Error");
}