#!/usr/bin/node
const { dict } = require('./101-data');

const occurrencesByUserId = {};

for (const userId in dict) {
  if (Object.prototype.hasOwnProperty.call(dict, userId)) {
    const occurrences = dict[userId];

    if (!Object.prototype.hasOwnProperty.call(occurrencesByUserId, occurrences)) {
      occurrencesByUserId[occurrences] = [];
    }

    occurrencesByUserId[occurrences].push(userId);
  }
}

console.log(occurrencesByUserId);
