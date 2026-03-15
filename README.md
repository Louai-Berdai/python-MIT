# Average Calculator in TypeScript

This is a TypeScript version of the Python program that calculates the average of four numbers entered by the user.

## Setup

1. Ensure you have Node.js installed (version 14 or higher).
2. Install dependencies: `npm install`
3. If you encounter script execution policy issues in PowerShell, run PowerShell as Administrator and execute: `Set-ExecutionPolicy RemoteSigned`

## Running the Program

Run the program with: `npm start`

Or directly with: `npx ts-node average_calculator.ts`

The program will prompt you to enter four numbers and then display their average.

## Notes

- The program uses Node.js's readline module for interactive input.
- Input validation ensures only valid numbers are accepted.
- The average is displayed with two decimal places.