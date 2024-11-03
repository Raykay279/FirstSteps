"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var readline = require("readline");
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.question('Bitte gib dein Alter ein: ', function (eingabe) {
    var alter = parseInt(eingabe);
    if (alter < 0 || alter > 120) {
        console.log("Unrealistisches alter");
    }
    else if (alter <= 11) {
        console.log("5 Euro");
    }
    else if (alter >= 12 && alter <= 17) {
        console.log("8 Euro");
    }
    else if (alter >= 18 && alter <= 64) {
        console.log("12 Euro");
    }
    else {
        console.log("6 Euro");
    }
    rl.close();
});
