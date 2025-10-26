const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

rl.question('', (inputs) => {
    const [a] = inputs.split(' ').map(Number);

    my_function(a);

    rl.close();
})

let my_function = (a) => {
    if(a >= 90){
        console.log('A');
    } 
    else if(a >= 80){
        console.log('B');
    }
    else if(a >= 70){
        console.log('C');
    }
    else if(a >= 60){
        console.log('D');
    }
    else{
        console.log('F');
    }
}