#!/usr/bin/env node
const args = process.argv.slice(2);  // Remove the first two elements (node executable and script path)
const firstArg = args.shift();  // Remove and retrieve the first argument

if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
