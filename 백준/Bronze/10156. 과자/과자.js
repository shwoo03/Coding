const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split(/\s+/).map(Number);

let [price, num, money] = input;

let total_price = price * num;

if (total_price > money) {
    console.log(total_price - money);
}
else{
    console.log(0);
}
