const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

const m = Number(input[0]);
const n = Number(input[1]);
const arr = [];

for (let i = Math.ceil(Math.sqrt(m)); i<=Math.floor(Math.sqrt(n)); i++){
    arr.push(i**2);
}

if (arr.length != 0) {
    // var temp = 0;
    // for (const num in arr)
    //     temp += num;
    // console.log(temp);
    console.log(arr.reduce((acc, i) => acc + i, 0));
    console.log(arr[0]);
}
else
    console.log(-1);