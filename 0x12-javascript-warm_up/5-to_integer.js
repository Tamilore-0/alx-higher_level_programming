#!/usr/bin/node

try {
  const parsedValue = parseInt(process.argv[2]);
  if (isNaN(parsedValue)) {
    throw new Error('Not a number');
  } else {
    console.log(`My number: ${parsedValue}`);
  }
} catch (error) {
  console.error(error.message); // Output: Custom error message
}
