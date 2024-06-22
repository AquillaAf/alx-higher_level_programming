#!/usr/bin/env node
const args = process.argv; // Remove the first two elements (node executable and script path)
if (args.length === 2) {
  console.log('No argument');
} else {
  for (let i = 2; i < args.length; i++) { console.log(args[i]); }
}
