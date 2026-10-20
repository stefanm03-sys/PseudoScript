const fs = require('fs'); // This is the File System module required for accessing files.
const { readFile } = require('fs/promises');
const { url } = require('inspector');
const p = document.getElementById(output);
const inputA = document.getElementById(input);
const button = document.getElementById(run);
const download = document.getElementById("file")
let output = "out";
let input = "in";
let run = "exec";
let psc = "define.py";


button.addEventListener("click", () => {
    let output = fs.access(define.py);
    p.textContent(output);
});

download.addEventListener("click", () => {
    let input = p.textContent
    let file = blob(input)
    let url = URL.createObjectURL(file)
    download.href = url
});


