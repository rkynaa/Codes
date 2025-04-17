// Parse nice int from char problem (8th Kyu)

/*
Task description:

You ask a small girl,"How old are you?" She always says, "x years old", where x is a random number between 0 and 9.

Write a program that returns the girl's age (0-9) as an integer.

Assume the test input string is always a valid string. 
For example, the test input may be "1 year old" or "5 years old". 
The first character in the string is always a number.
*/

// Define a function to extract the age from a string like "4 years old"
function getAge(inputString) {
    // Convert the first character of the input string to a string (in case it's not),
    // then parse it as an integer using parseInt.
    // Assumes the age is always the first character in the string.
    return parseInt(String(inputString[0]));
}