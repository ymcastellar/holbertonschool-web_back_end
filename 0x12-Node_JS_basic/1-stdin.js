const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question('Welcome to Holberton School, what is your name?\n', (ans) => {
  console.log(`Your name is: ${ans}`);
  console.log('This important software is now closing');
  process.exit();
});
