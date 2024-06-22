#!/usr/bin/node
const args = process.argv;
if (args.length === 2) {
  console.log('Not a number');
} else if (args.length === 3) {
  const value = Number(args[2]);
  if (isNaN(value) === true) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + value);
  }
}
