// TypeScript program to calculate the average of four numbers entered by the user

import * as readline from 'readline';

function main(): void {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log("Enter four numbers to calculate their average:");

    const numbers: number[] = [];
    let count = 0;

    function ask(): void {
        if (count < 4) {
            rl.question(`Number ${count + 1}: `, (answer: string) => {
                const num = parseFloat(answer);
                if (isNaN(num)) {
                    console.log("Invalid input. Please enter a valid number.");
                    ask();
                } else {
                    numbers.push(num);
                    count++;
                    ask();
                }
            });
        } else {
            rl.close();
            const average = numbers.reduce((a, b) => a + b, 0) / 4;
            console.log(`The average of ${numbers.join(', ')} is: ${average.toFixed(2)}`);
        }
    }

    ask();
}

main();