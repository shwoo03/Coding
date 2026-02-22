const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');

const [a, b, c] = input;
const [d, e] = input.slice(3);

const min_abc = Math.min(a, b, c);
const min_de = Math.min(d, e);

const result = min_abc + min_de - 50;
console.log(result);