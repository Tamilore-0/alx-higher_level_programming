#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
const valuesArray = Object.values(dict);

for (const key in dict) {
  //check if ley already exists
  if (dict[key] in newDict) {
    //check if value already exists
    if (!(key in valuesArray)) {
      newDict[dict[key]].push(key);
    }
  } else {
    newDict[dict[key]] = [key];
  }
}
console.log(newDict);
