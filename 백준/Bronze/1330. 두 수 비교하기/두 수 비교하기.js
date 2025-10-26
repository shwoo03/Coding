const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.on('line', (input) => {
    const [a, b] = input.split(' ').map(Number);
    if(a > b){
        console.log(">");
    } else if(a < b){
        console.log("<");
    } else {
        console.log("==");
    }
    rl.close();
});
