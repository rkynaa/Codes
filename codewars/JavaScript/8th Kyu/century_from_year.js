// Century From Year (8th Kyu)

/*
Task description:

Introduction

The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task

Given a year, return the century it is in.

Examples

1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
2742 --> 28

Note: this kata uses strict construction as shown in the description and the examples, you can read more about it here
*/

// Define a function to determine the century of a given year
function century(year) {
    // Calculate the remainder when the year is divided by 100
    // This tells us if the year is at the end of a century (e.g., 1900) or in the middle of one (e.g., 1901)
    var rem = year % 100;

    // Calculate the base century by dividing the year by 100 and rounding down
    var res = Math.floor(year / 100);

    // If there's a remainder, the year is in the next century
    // e.g., 1901 → 20th century (not 19th)
    if (rem > 0) {
        return res + 1;
    }

    // If no remainder, return the exact century
    // e.g., 2000 → 20th century
    return res;
}