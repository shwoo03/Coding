const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split(/\s+/).map(Number);

let [hour, minute, second] = input.slice(0, 3);
let need_second = input[3];

second += Math.floor(need_second % 60);
if(second >= 60){
    minute += Math.floor(second / 60);
    second = second % 60;
}

minute += Math.floor(need_second / 60) % 60;
if(minute >= 60){
    hour += Math.floor(minute / 60);
    minute = minute % 60;
}

hour += Math.floor(need_second / 3600);
if(hour >= 24){
    hour = hour % 24;
}

console.log(`${hour} ${minute} ${second}`);