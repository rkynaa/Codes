// Fix string case (7th Kyu)

/*
Task description:

In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

    make as few changes as possible.
    if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.

For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

More examples in test cases. Good luck!

Please also try:

Simple time difference

Simple remove duplicates
*/

// Define a function that converts a string to either all lowercase or all uppercase,
// depending on which case is more frequent in the string.
function solve(s) {
    var nLow, nUpp;
    nLow = nUpp = 0;  // Initialize counters for lowercase and uppercase characters

    // Loop through each character in the string
    for (i = 0; i < s.length; i++) {
        // Check if the character is uppercase
        if (s[i] == s[i].toUpperCase()) {
            nUpp++;  // Increment uppercase counter
        } else {
            nLow++;  // Increment lowercase counter
        }
    }

    // If there are more lowercase letters (or equal), convert the whole string to lowercase
    if (nLow >= nUpp) {
        s = s.toLowerCase();
    } else {
        // Otherwise, convert the string to uppercase
        s = s.toUpperCase();
    }

    // Return the modified string
    return s;
}