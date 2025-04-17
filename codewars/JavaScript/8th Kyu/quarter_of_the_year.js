// Quarter of the year (8th Kyu)

/*
Task description:

Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

Constraint:

    1 <= month <= 12
*/

// Define an arrow function that returns the quarter of the year for a given month
// Parameter:
//   month - an integer from 1 to 12 representing the month
const quarterOf = (month) => {
    // Months 1, 2, 3 → Quarter 1
    if (month < 4) return 1;

    // Months 4, 5, 6 → Quarter 2
    if (month < 7) return 2;

    // Months 7, 8, 9 → Quarter 3
    if (month < 10) return 3;

    // Months 10, 11, 12 → Quarter 4
    return 4;
}  