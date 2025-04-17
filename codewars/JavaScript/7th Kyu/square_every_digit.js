// Square Every Digit (7th Kyu)

/*
Task description:

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!
*/

// Define a function that squares each digit of a number and concatenates the results
function squareDigits(num) {
    var res = "";  // Initialize an empty string to build the result

    // Convert the number to a string and loop through each digit
    for (i = 0; i < String(num).length; i++) {
        // Convert the current character back to an integer, square it,
        // then convert the result back to a string and append to 'res'
        res += String(parseInt(String(num)[i]) ** 2);
    }

    // Convert the final concatenated string back to an integer and return it
    return parseInt(res);
}