const fs = require('fs'); // This is the File System module required for accessing files.
const { readFile } = require('fs/promises');
const p = document.getElementById(output);
const inputA = document.getElementById(input);
const button = document.getElementById(run);
let output = "out";
let input = "in";
let run = "exec";
let psc = "define.py";


button.addEventListener("click", () => {
    let output = fs.read(psc.execute());
    p.textContent(output);
});

if (inputA) {
    return inputA;
};



